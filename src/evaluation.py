# src/evaluation.py

import joblib
import pandas as pd
from pathlib import Path
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score
)

# -------------------------------------------------------------------
# ۱. تعیین مسیرها (مستقل از پوشه ترمینال)
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "artifacts" / "model.joblib"

# -------------------------------------------------------------------
# ۲. بارگذاری داده و تقسیم آن (همان تقسیم اولیه با random_state=42)
# -------------------------------------------------------------------
def load_and_split_data():
    """بارگذاری داده و تقسیم آن به آموزش و آزمون."""
    dataset = load_breast_cancer(as_frame=True)
    df = dataset.frame.copy()
    
    X = df.drop(columns=["target"])
    y = df["target"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    
    return X_train, X_test, y_train, y_test

# -------------------------------------------------------------------
# ۳. بررسی آماده‌بودن داده‌ها (چک‌لیست)
# -------------------------------------------------------------------
def check_data_readiness(X_train, X_test, y_train, y_test):
    """بررسی آماده‌بودن داده‌ها و ساختار Pipeline."""
    print("=== بررسی آماده‌بودن داده‌ها ===")
    print("X_train shape:", X_train.shape)  # باید (455, 30) باشد
    print("X_test shape:", X_test.shape)    # باید (114, 30) باشد
    print("y_train shape:", y_train.shape)  # باید (455,) باشد
    print("y_test shape:", y_test.shape)    # باید (114,) باشد
    
    # بررسی Pipeline
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=2000))
    ])
    print("Pipeline steps:", model.steps)
    
    # بررسی Baseline
    baseline = DummyClassifier(strategy="most_frequent")
    print("Baseline:", baseline)
    
    print("\n✅ بررسی اولیه انجام شد. (توجه: X_test و y_test نباید در Cross-validation استفاده شوند.)\n")

# -------------------------------------------------------------------
# ۴. اجرای Cross-validation روی داده آموزش
# -------------------------------------------------------------------
def run_cross_validation(X_train, y_train):
    """اجرای Cross-validation با StratifiedKFold روی داده آموزش."""
    print("=== اجرای Cross-validation ===")
    
    cv_model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=2000))
    ])
    
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    scoring = {
        "accuracy": "accuracy",
        "balanced_accuracy": "balanced_accuracy",
        "f1_macro": "f1_macro"
    }
    
    cv_results = cross_validate(
        cv_model, X_train, y_train, cv=cv, scoring=scoring, return_train_score=False
    )
    
    # چاپ نتایج
    for metric in scoring:
        scores = cv_results[f'test_{metric}']
        print(f"{metric}: {scores}")
        print(f"Mean: {scores.mean():.4f}")
        print(f"Std: {scores.std():.4f}")
        print()
    
    return cv_results

# -------------------------------------------------------------------
# ۵. ارزیابی نهایی روی Test Set (فقط یک بار)
# -------------------------------------------------------------------
def evaluate_final_model(X_train, X_test, y_train, y_test):
    """آموزش مدل نهایی و ارزیابی روی Test Set."""
    print("=== ارزیابی نهایی روی Test Set ===")
    
    # آموزش مدل نهایی
    final_model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=2000))
    ])
    final_model.fit(X_train, y_train)
    
    # پیش‌بینی
    predictions = final_model.predict(X_test)
    
    # محاسبه معیارها
    print("Accuracy:", accuracy_score(y_test, predictions))
    print("Balanced Accuracy:", balanced_accuracy_score(y_test, predictions))
    print("F1 Macro:", f1_score(y_test, predictions, average="macro"))
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))
    
    return final_model, predictions

# -------------------------------------------------------------------
# ۶. مقایسه با Baseline
# -------------------------------------------------------------------
def compare_with_baseline(X_train, X_test, y_train, y_test):
    """آموزش Baseline و مقایسه با مدل اصلی."""
    print("\n=== مقایسه با Baseline ===")
    
    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(X_train, y_train)
    baseline_predictions = baseline.predict(X_test)
    
    # محاسبه معیارهای Baseline
    baseline_accuracy = accuracy_score(y_test, baseline_predictions)
    baseline_balanced_accuracy = balanced_accuracy_score(y_test, baseline_predictions)
    baseline_f1_macro = f1_score(y_test, baseline_predictions, average="macro")
    
    print("Baseline Accuracy:", baseline_accuracy)
    print("Baseline Balanced Accuracy:", baseline_balanced_accuracy)
    print("Baseline F1 Macro:", baseline_f1_macro)
    
    return baseline_predictions

# -------------------------------------------------------------------
# ۷. تحلیل خطاها
# -------------------------------------------------------------------
def analyze_errors(X_test, y_test, predictions):
    """استخراج و نمایش خطاهای مدل."""
    print("\n=== تحلیل خطاها ===")
    
    error_analysis = X_test.copy()
    error_analysis["actual"] = y_test
    error_analysis["predicted"] = predictions
    
    errors = error_analysis[error_analysis["actual"] != error_analysis["predicted"]]
    
    print("Number of errors:", len(errors))
    print(errors.head())

# -------------------------------------------------------------------
# ۸. تابع اصلی (Main)
# -------------------------------------------------------------------
def main():
    # ۱. بارگذاری و تقسیم داده
    X_train, X_test, y_train, y_test = load_and_split_data()
    
    # ۲. بررسی آماده‌بودن
    check_data_readiness(X_train, X_test, y_train, y_test)
    
    # ۳. اجرای Cross-validation
    run_cross_validation(X_train, y_train)
    
    # ۴. ارزیابی نهایی
    final_model, predictions = evaluate_final_model(X_train, X_test, y_train, y_test)
    
    # ۵. مقایسه با Baseline
    compare_with_baseline(X_train, X_test, y_train, y_test)
    
    # ۶. تحلیل خطاها
    analyze_errors(X_test, y_test, predictions)

if __name__ == "__main__":
    main()