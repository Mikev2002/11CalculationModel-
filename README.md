# 11CalculationModel-

Module 11: Calculation Model (FastAPI + SQLAlchemy + Pydantic + CI/CD)

This project implements a Calculation Model using:

FastAPI

SQLAlchemy ORM

Pydantic v2 validation

Optional Factory Pattern

Automated testing with Pytest

CI/CD with GitHub Actions

Docker containerization + deployment to Docker Hub

This fulfills Module 11: Implement and Test a Calculation Model.

🚀 Features
✅ SQLAlchemy Calculation Model

Stores:

a

b

type (Add, Sub, Multiply, Divide)

result

✅ Pydantic v2 Schemas

Includes strong validation:

Valid calculation types

Zero-division prevention

Correct field ordering for v2 validation

✅ Factory Pattern

Encapsulates all calculation logic:

Add → a + b  
Sub → a - b  
Multiply → a * b  
Divide → a / b  


The backend calls the factory to compute the result before saving to the database.

✅ Fully Tested

Includes:

Unit tests for factory & schema validations

Integration tests for /calculate endpoint

Basic FastAPI root test

All tests run automatically in GitHub Actions.

⚙️ How to Run the App Locally
1. Create virtual environment
python -m venv venv

2. Activate it

Windows:

venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt


(or install packages manually)

4. Start the app
uvicorn app.main:app --reload


FastAPI docs will be available at:
👉 http://127.0.0.1:8000/docs

🧪 How to Run Tests Locally
pytest -s


All tests must pass:

Unit tests

Integration tests

Validation tests

🐋 Docker Instructions
Build image
docker build -t calc-model .

Run container
docker run -p 8000:8000 calc-model

Docker Hub Repository

Your GitHub Actions workflow automatically builds & pushes:

docker.io/mikev424/calc-model:latest

🔄 CI/CD Pipeline

The .github/workflows/ci.yml pipeline:

Installs dependencies

Spins up PostgreSQL service

Runs all tests

Logs into Docker Hub using GitHub Secrets

Builds & pushes Docker image

Marks the build as passed/failed

Secrets required:

DOCKER_USERNAME = mikev424
DOCKER_PASSWORD = <your token>

📬 API Endpoint
POST /calculate

Request

{
  "a": 10,
  "b": 5,
  "type": "Divide"
}


Response

{
  "id": 1,
  "a": 10,
  "b": 5,
  "type": "Divide",
  "result": 2
}

📝 Files Included
app/
  main.py
  database.py
  models/
      calculation.py
  schemas/
      calculation.py
  services/
      calculation_factory.py

tests/
  conftest.py
  test_app_basic.py
  test_calculation_unit.py
  test_calculation_integration.py

Dockerfile
.github/workflows/ci.yml

🎯 Learning Outcomes Demonstrated

Created a SQLAlchemy model

Implemented and validated a Pydantic schema

Added factory pattern for extensibility

Implemented unit and integration testing

Configured a GitHub Actions CI/CD workflow

Containerized the application with Docker

Connected Python, PostgreSQL, and FastAPI