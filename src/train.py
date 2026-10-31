# src/train.py

import os
import joblib
import pandas as pd
from pathlib import Path
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ۱. تعیین مسیرها به صورت مطلق (مستقل از پوشه‌ای که ترمینال در آن باز است)
BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACT_DIR = BASE_DIR / "artifacts"
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

# تعریف مسیرها به صورت سراسری (Global) تا در فایل‌های دیگر قابل ایمپورت باشند
MODEL_PATH = ARTIFACT_DIR / "model2.joblib"
TEST_DATA_PATH = ARTIFACT_DIR / "test_data.joblib"

def main():
    # ۲. بارگذاری داده
    dataset = load_breast_cancer(as_frame=True)
    df = dataset.frame.copy()

    # ۳. تعریف ویژگی‌ها و متغیر هدف
    X = df.drop(columns=["target"])
    y = df["target"]

    # ۴. تقسیم داده
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # ۵. ذخیره داده‌های آزمون برای استفاده در predict.py (بدون تعریف مجدد متغیر)
    joblib.dump((X_test, y_test), TEST_DATA_PATH)
    print(f"Test data saved to: {TEST_DATA_PATH}")
    
    # ۶. آموزش Baseline
    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(X_train, y_train)
    baseline_predictions = baseline.predict(X_test)
    baseline_accuracy = accuracy_score(y_test, baseline_predictions)
    print(f"Baseline Accuracy: {baseline_accuracy:.4f}")

    # ۷. آموزش Pipeline مدل اصلی
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=2000))
    ])
    model.fit(X_train, y_train)
    print("Model trained successfully.")

    # ۸. محاسبه معیارهای ارزیابی
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)
    f1 = f1_score(y_test, predictions, zero_division=0)

    print(f"Model Accuracy:  {accuracy:.4f}")
    print(f"Model Precision: {precision:.4f}")
    print(f"Model Recall:    {recall:.4f}")
    print(f"Model F1-score:  {f1:.4f}")

    # ۹. ذخیره Pipeline آموزش‌دیده
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to: {MODEL_PATH}")

if __name__ == "__main__":
    main()