from fastapi import FastAPI
from pydantic import BaseModel , Field
from typing import Literal



class StudentData(BaseModel):
    age : int = Field(..., gt=0, description="Age of the student in years")

    gender :Literal["Male","Female"]

    country: str 

    academic_level: Literal[
    "Undergraduate",
    "Graduate",
    "High School"
]

    most_used_platform : Literal['Facebook', 'LinkedIn', 'Instagram', 'Snapchat','Twitter','YouTube', 'TikTok', 'LINE', 'KakaoTalk', 'VKontakte', 'WhatsApp','WeChat']

    purpose_of_use : Literal["Networking","Education","Entertainment","News"]

    avg_daily_usage_hours : float = Field(...,ge=0,le=24)

    daily_unlocks:int =Field(...,ge = 0)

    study_hours : float = Field(...,ge=0)

    physical_activity_hours: float =Field(...,ge=0)

    sleep_hours_per_night:float = Field(...,ge=0 , le=24)

    stress_level: Literal["Medium","Low","Very High","High"]




class PredictionResponse(BaseModel):
    predicted_mental_health_score: float
