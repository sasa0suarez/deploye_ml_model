import sys
from pathlib import Path
from enum import Enum  

# Add parent dir to path
parent_dir = Path(__file__).resolve().parent.parent
if str(parent_dir) not in sys.path:
    sys.path.append(str(parent_dir))

from config import MODEL_PATH
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Medical Charges Prediction API")

# Load model
model = joblib.load(MODEL_PATH)


class SexEnum(str, Enum):
    male = "male"
    female = "female"

class SmokerEnum(str, Enum):
    yes = "yes"
    no = "no"

class RegionEnum(str, Enum):
    northeast = "northeast"
    northwest = "northwest"
    southeast = "southeast"
    southwest = "southwest"


class PatientData(BaseModel):
    age: int
    sex: SexEnum        
    bmi: float
    children: int
    smoker: SmokerEnum  
    region: RegionEnum   

@app.get("/")
def home():
    return {"message": "Welcome to the Medical Charges Prediction API! Go to /docs to test it."}

@app.post("/predict")
def predict_charges(data: PatientData):
    input_df = pd.DataFrame([data.model_dump()])
    prediction = model.predict(input_df)
    return {"predicted_charges": round(float(prediction[0]), 2)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)