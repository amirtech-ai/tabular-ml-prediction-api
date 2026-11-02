# prediction/tests.py

import json
import numpy as np
import pandas as pd
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch
from pathlib import Path
from .constants import FEATURE_NAMES

# -------------------------------------------------------------------
# Fixtures (داده‌های آماده برای تست)
# -------------------------------------------------------------------
VALID_INPUT = {feature: 10.0 for feature in FEATURE_NAMES}


# ===================================================================
# ۱. تست‌های واحد (Unit Tests) - اعتبارسنجی داده‌ها
# ===================================================================
class UnitValidationTests(TestCase):
    """تست‌های مربوط به منطق اعتبارسنجی داده‌ها."""

    def test_valid_input(self):
        """تمام ویژگی‌های الزامی وجود دارند."""
        self.assertEqual(len(VALID_INPUT), 30)

    def test_missing_feature(self):
        """یک ویژگی الزامی حذف شده است."""
        incomplete = VALID_INPUT.copy()
        del incomplete[FEATURE_NAMES[0]]
        self.assertEqual(len(incomplete), 29)

    def test_extra_feature(self):
        """یک ویژگی اضافی ارسال شده است."""
        extra = VALID_INPUT.copy()
        extra['extra_feature'] = 10.0
        self.assertEqual(len(extra), 31)

    def test_non_numeric_value(self):
        """مقدار یک ویژگی به رشته‌ی غیر عددی تبدیل شده است."""
        invalid = VALID_INPUT.copy()
        invalid[FEATURE_NAMES[0]] = "not_a_number"
        self.assertIsInstance(invalid[FEATURE_NAMES[0]], str)

    def test_nan_value(self):
        """مقدار NaN ارسال شده است."""
        nan_input = VALID_INPUT.copy()
        nan_input[FEATURE_NAMES[0]] = float('nan')
        self.assertTrue(np.isnan(nan_input[FEATURE_NAMES[0]]))

    def test_infinity_value(self):
        """مقدار بی‌نهایت ارسال شده است."""
        inf_input = VALID_INPUT.copy()
        inf_input[FEATURE_NAMES[0]] = float('inf')
        self.assertTrue(np.isinf(inf_input[FEATURE_NAMES[0]]))


# ===================================================================
# ۲. تست‌های API (API Tests) - مسیرهای اصلی
# ===================================================================
class APITests(TestCase):
    """تست‌های مربوط به مسیرهای اصلی API (Health و Predict)."""

    def setUp(self):
        self.client = APIClient()

    # ------------------- مسیر سلامت -------------------
    def test_health_check_success(self):
        """تست مسیر سلامت: باید پاسخ 200 با وضعیت ok برگرداند."""
        response = self.client.get('/api/v1/health/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')

    # ------------------- درخواست معتبر -------------------
    def test_predict_valid_input(self):
        """تست درخواست معتبر: باید پاسخ 200 با ساختار درست برگرداند."""
        response = self.client.post(
            '/api/v1/predict/',
            data=json.dumps(VALID_INPUT),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertIn('prediction', response.data)
        self.assertIn('probabilities', response.data)
        self.assertIn(response.data['prediction'], [0, 1])
        self.assertIsInstance(response.data['prediction'], int)
        self.assertIsInstance(response.data['probabilities']['malignant'], float)
        self.assertIsInstance(response.data['probabilities']['benign'], float)

    # ------------------- ورودی‌های نامعتبر -------------------
    def test_predict_empty_body(self):
        """تست بدنه‌ی خالی: باید پاسخ 400 بدهد."""
        response = self.client.post('/api/v1/predict/', data={}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_missing_feature(self):
        """تست فیلد الزامی مفقود: باید پاسخ 400 بدهد."""
        incomplete_input = VALID_INPUT.copy()
        del incomplete_input[FEATURE_NAMES[0]]
        response = self.client.post('/api/v1/predict/', data=json.dumps(incomplete_input), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_extra_feature(self):
        """تست ویژگی اضافی: باید پاسخ 400 بدهد."""
        extra_input = VALID_INPUT.copy()
        extra_input['extra_feature'] = 10.0
        response = self.client.post('/api/v1/predict/', data=json.dumps(extra_input), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_non_numeric_value(self):
        """تست مقدار غیر عددی: باید پاسخ 400 بدهد."""
        invalid_input = VALID_INPUT.copy()
        invalid_input[FEATURE_NAMES[0]] = "not_a_number"
        response = self.client.post('/api/v1/predict/', data=json.dumps(invalid_input), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_nan_value(self):
        """تست مقدار NaN: باید پاسخ 400 بدهد."""
        nan_input = VALID_INPUT.copy()
        nan_input[FEATURE_NAMES[0]] = float('nan')
        response = self.client.post('/api/v1/predict/', data=json.dumps(nan_input), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_infinity_value(self):
        """تست مقدار Infinity: باید پاسخ 400 بدهد."""
        inf_input = VALID_INPUT.copy()
        inf_input[FEATURE_NAMES[0]] = float('inf')
        response = self.client.post('/api/v1/predict/', data=json.dumps(inf_input), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_invalid_json(self):
        """تست JSON نامعتبر: باید پاسخ 400 بدهد."""
        response = self.client.post('/api/v1/predict/', data="This is not a JSON", content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# ===================================================================
# ۳. تست‌های یکپارچگی مدل (Model Integrity Tests)
# ===================================================================
class ModelIntegrityTests(TestCase):
    """تست‌های مربوط به بارگذاری مدل و جلوگیری از آموزش مجدد."""

    def setUp(self):
        self.client = APIClient()

    def test_model_loaded(self):
        """مدل ذخیره‌شده بارگذاری می‌شود."""
        from prediction.views import MODEL
        self.assertIsNotNone(MODEL, "Model should be loaded. Check MODEL_PATH and artifacts/model.joblib.")

    def test_no_retraining(self):
        """مسیر API باعث آموزش مجدد مدل نمی‌شود."""
        with patch('sklearn.linear_model.LogisticRegression.fit') as mock_fit:
            self.client.post('/api/v1/predict/', data=json.dumps(VALID_INPUT), content_type='application/json')
            mock_fit.assert_not_called()

    @patch('prediction.views.MODEL', None)
    def test_predict_without_model(self):
        """تست عدم وجود مدل: باید پاسخ 500 بدهد، نه اینکه به صورت خاموش ادامه دهد."""
        response = self.client.post('/api/v1/predict/', data=json.dumps(VALID_INPUT), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)


# ===================================================================
# ۴. تست‌های End-to-End و ترکیبی (Integration)
# ===================================================================
class EndToEndTests(TestCase):
    """تست‌های ترکیبی و مسیر کامل از ورودی تا خروجی."""

    def setUp(self):
        self.client = APIClient()

    def test_end_to_end_prediction(self):
        """مسیر کامل: درخواست -> اعتبارسنجی -> مدل -> پاسخ."""
        response = self.client.post(
            '/api/v1/predict/',
            data=json.dumps(VALID_INPUT),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'success')

    def test_order_of_features(self):
        """تست ترتیب ویژگی‌ها: جابه‌جایی نامحسوس ستون‌ها نباید نتیجه را تغییر دهد."""
        import random
        # ساخت دو ورودی با ترتیب‌های مختلف
        keys = list(VALID_INPUT.keys())
        random.shuffle(keys)
        shuffled_input = {k: VALID_INPUT[k] for k in keys}

        response1 = self.client.post('/api/v1/predict/', data=json.dumps(VALID_INPUT), content_type='application/json')
        response2 = self.client.post('/api/v1/predict/', data=json.dumps(shuffled_input), content_type='application/json')

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response1.data['prediction'], response2.data['prediction'])

    def test_all_features_required(self):
        """تست تک‌تک ویژگی‌ها: هر ویژگی که حذف شود باید خطا بدهد."""
        for feature in FEATURE_NAMES:
            incomplete = VALID_INPUT.copy()
            del incomplete[feature]
            response = self.client.post('/api/v1/predict/', data=json.dumps(incomplete), content_type='application/json')
            self.assertEqual(response.status_code, 400, f"Missing feature '{feature}' did not raise 400.")