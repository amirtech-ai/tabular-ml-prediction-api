# prediction/tests.py

import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch
from .constants import FEATURE_NAMES

# یک نمونه داده‌ی معتبر برای تست (۳۰ ویژگی با مقدار ۱۰.۰)
VALID_INPUT = {feature: 10.0 for feature in FEATURE_NAMES}


class PredictionAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    # ------------------- تست‌های مسیر سلامت -------------------
    def test_health_check_success(self):
        """تست مسیر سلامت: باید پاسخ 200 با وضعیت ok برگرداند."""
        response = self.client.get('/api/v1/health/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')

    # ------------------- تست‌های درخواست معتبر -------------------
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

    # ------------------- تست‌های ورودی نامعتبر -------------------
    def test_predict_empty_body(self):
        """تست بدنه‌ی خالی: باید پاسخ 400 بدهد."""
        response = self.client.post(
            '/api/v1/predict/',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_missing_feature(self):
        """تست فیلد الزامی مفقود: باید پاسخ 400 بدهد."""
        incomplete_input = VALID_INPUT.copy()
        del incomplete_input[FEATURE_NAMES[0]]  # حذف یکی از ویژگی‌ها
        response = self.client.post(
            '/api/v1/predict/',
            data=json.dumps(incomplete_input),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_extra_feature(self):
        """تست ویژگی اضافی: باید پاسخ 400 بدهد."""
        extra_input = VALID_INPUT.copy()
        extra_input['extra_feature'] = 10.0
        response = self.client.post(
            '/api/v1/predict/',
            data=json.dumps(extra_input),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_non_numeric_value(self):
        """تست مقدار غیر عددی: باید پاسخ 400 بدهد."""
        invalid_input = VALID_INPUT.copy()
        invalid_input[FEATURE_NAMES[0]] = "not_a_number"
        response = self.client.post(
            '/api/v1/predict/',
            data=json.dumps(invalid_input),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_nan_value(self):
        """تست مقدار NaN: باید پاسخ 400 بدهد."""
        nan_input = VALID_INPUT.copy()
        nan_input[FEATURE_NAMES[0]] = float('nan')
        response = self.client.post(
            '/api/v1/predict/',
            data=json.dumps(nan_input),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_infinity_value(self):
        """تست مقدار Infinity: باید پاسخ 400 بدهد."""
        inf_input = VALID_INPUT.copy()
        inf_input[FEATURE_NAMES[0]] = float('inf')
        response = self.client.post(
            '/api/v1/predict/',
            data=json.dumps(inf_input),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_predict_invalid_json(self):
        """تست JSON نامعتبر: باید پاسخ 400 بدهد."""
        response = self.client.post(
            '/api/v1/predict/',
            data="This is not a JSON",
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ModelLoadingTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('prediction.views.MODEL', None)
    def test_predict_without_model(self):
        """تست عدم وجود مدل: باید پاسخ 500 بدهد، نه اینکه به صورت خاموش ادامه دهد."""
        response = self.client.post(
            '/api/v1/predict/',
            data=json.dumps(VALID_INPUT),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)