# src/predict.py

import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "artifacts" / "model2.joblib"
TEST_DATA_PATH = BASE_DIR / "artifacts" / "test_data.joblib" # مسیر داده‌های آزمون

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Trained model not found: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def predict(input_data):
    model = load_model()
    if isinstance(input_data, dict):
        input_data = pd.DataFrame([input_data])
    if input_data.shape[1] != 30:
        raise ValueError(f"Expected 30 features, but got {input_data.shape[1]}.")
    
    predictions = model.predict(input_data)
    probabilities = model.predict_proba(input_data)
    return predictions, probabilities

if __name__ == "__main__":
    print("--- Test on Unseen Data (Test Set) ---")
    
    # ۱. بارگذاری داده‌های آزمون که در train.py ذخیره کردیم
    if not TEST_DATA_PATH.exists():
        raise FileNotFoundError(f"Test data not found: {TEST_DATA_PATH}. Please run train.py first.")
    
    X_test, y_test = joblib.load(TEST_DATA_PATH)
    
    # ۲. انتخاب یک نمونه از داده‌های آزمون
    sample = X_test.head(1)
    actual_label = y_test.head(1).values[0]
    
    # ۳. انجام پیش‌بینی
    preds, probs = predict(sample)
    
    # ۴. چاپ نتایج
    print(f"Actual Label:    {actual_label} (0=malignant, 1=benign)")
    print(f"Predicted Label: {preds[0]}")
    print(f"Probabilities:   {probs[0]}")
    
    if actual_label == preds[0]:
        print("Result: ✅ Correct prediction!")
    else:
        print("Result: ❌ Incorrect prediction.")