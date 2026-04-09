from pydantic import BaseModel

class PatientData(BaseModel):
    age: int
    blood_pressure: float
    cholesterol: float
