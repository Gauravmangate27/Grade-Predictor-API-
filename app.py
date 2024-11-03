import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Step 1: Load the model from the .pkl file
with open('linear_regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Create FastAPI instance
app = FastAPI()

# Define a request model using Pydantic
class InputData(BaseModel):
    Previous_Grades: float
    Attendance: float
    Study_Hours: float
    Educational_Resources: float
    Study_Space: float

# Step 2: Create a prediction endpoint
@app.post("/predict/")
async def predict(input_data: InputData):
    # Create a DataFrame from the input data
    input_df = pd.DataFrame({
        'Previous_Grades': [input_data.Previous_Grades],
        'Attendance': [input_data.Attendance],
        'Study_Hours': [input_data.Study_Hours],
        'Educational_Resources': [input_data.Educational_Resources],
        'Study_Space': [input_data.Study_Space]
    })

    # Step 3: Make predictions
    predictions = loaded_model.predict(input_df)

    # Return the predictions
    return {"Predicted Grade": predictions[0]}
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=5000)

# To run the application, use the following command in the terminal:
# uvicorn your_filename:app --reload
