from fastapi import APIRouter

from backend.schemas.prediction import StudentData , PredictionResponse

from backend.services.prediction_service import Predict_mental_health


router = APIRouter()

@router.post("/predict" , response_model = PredictionResponse)

def predict(data:StudentData):

    prediction = Predict_mental_health(data)

    return PredictionResponse(predicted_mental_health_score=prediction)
