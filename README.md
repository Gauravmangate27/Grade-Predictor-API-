# Grade-Predictor-API-
# GradePredictorAPI 🎓

## Project Overview
**GradePredictorAPI** is a web application that utilizes machine learning to predict student grades based on various academic and environmental factors. This API is designed to provide valuable insights for students, educators, and parents to understand the critical factors influencing academic performance.

## Features
- **User-Friendly API**: Built with FastAPI for easy data input and real-time predictions.
- **Predictive Analytics**: Utilizes a linear regression model to assess the impact of various factors on student grades.
- **Interactive Documentation**: Auto-generated documentation via Swagger UI for seamless API interaction.
- **Data-Driven Insights**: Enables stakeholders to make informed decisions based on predictive analytics.

## Input Parameters
The API accepts the following input parameters, all scaled from **0 to 2**:
- **Previous Grades**: 
  - 0: Low
  - 1: Medium
  - 2: High
- **Attendance**: 
  - 0 to 100
- **Study Hours**: Numeric value representing hours studied.
- **Educational Resources**: 
  - 0: Low
  - 1: Medium
  - 2: High
- **Study Space**: 
  - 0: Low
  - 1: Medium
  - 2: High

The **Predicted Grade** will also be provided on the same scale from **0 to 2**.

## Technologies Used
- **FastAPI**: For building the web application and API endpoints.
- **Uvicorn**: ASGI server for running the application.
- **Pandas**: For data manipulation and preprocessing.
- **Scikit-learn**: For implementing the machine learning model.
- **Pickle**: For model serialization and loading.

## Getting Started
### Prerequisites
Make sure you have Python 3.6 or higher installed, along with pip.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Gauravmangate27/GradePredictorAPI.git
   cd GradePredictorAPI
