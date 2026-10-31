# prediction/views.py

import joblib
import pandas as pd
from pathlib import Path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionInputSerializer
from .constants import FEATURE_NAMES

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "artifacts" / "model2.joblib"

# تابع بارگذاری مدل
def load_model():
    """بارگذاری مدل از فایل"""
    if not MODEL_PATH.exists():
        return None
    try:
        return joblib.load(MODEL_PATH)
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# بارگذاری مدل در زمان شروع سرویس
MODEL = load_model()

@api_view(['GET'])
def health_check(request):
    if MODEL is None:
        return Response(
            {"status": "error", "message": "Model not loaded."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return Response({"status": "ok", "message": "Service is running."}, status=status.HTTP_200_OK)

@api_view(['POST'])
def predict(request):
    serializer = PredictionInputSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {"status": "error", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if MODEL is None:
        return Response(
            {"status": "error", "message": "Model is not available."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    validated_data = serializer.validated_data
    input_df = pd.DataFrame([[validated_data[feature] for feature in FEATURE_NAMES]], columns=FEATURE_NAMES)
    
    try:
        prediction = MODEL.predict(input_df)[0]
        probabilities = MODEL.predict_proba(input_df)[0]
        
        response_data = {
            "status": "success",
            "prediction": int(prediction),
            "probabilities": {
                "malignant": float(probabilities[0]),
                "benign": float(probabilities[1])
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        print(f"Model prediction error: {e}")
        return Response(
            {"status": "error", "message": "Internal prediction error."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )