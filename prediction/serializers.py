# prediction/serializers.py

from rest_framework import serializers
from .constants import FEATURE_NAMES

class PredictionInputSerializer(serializers.Serializer):
    """
    سریالایزر برای اعتبارسنجی ورودی API.
    این سریالایزر ۳۰ فیلد عددی را دریافت و اعتبارسنجی می‌کند.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # به صورت داینامیک ۳۰ فیلد عددی را به سریالایزر اضافه می‌کنیم
        for feature in FEATURE_NAMES:
            self.fields[feature] = serializers.FloatField(required=True)

    def to_internal_value(self, data):
        """
        این متد قبل از اعتبارسنجی اصلی اجرا می‌شود.
        اگر تعداد کلیدهای ارسال‌شده بیشتر از تعداد ویژگی‌های مورد انتظار باشد، خطا می‌دهد.
        """
        if len(data) > len(FEATURE_NAMES):
            raise serializers.ValidationError(
                {"error": f"Expected {len(FEATURE_NAMES)} features, but got {len(data)}. Extra features are not allowed."}
            )
        return super().to_internal_value(data)
    
    def validate(self, data):
        """
        اعتبارسنجی‌های تکمیلی:
        ۱. رد کردن مقادیر NaN یا Infinity
        """
        for key, value in data.items():
            if value in [float('nan'), float('inf'), float('-inf')]:
                raise serializers.ValidationError({
                    key: "This field cannot be NaN or Infinity."
                })
        return data