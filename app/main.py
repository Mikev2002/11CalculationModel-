from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate, CalculationRead
from app.services.calculation_factory import CalculationFactory

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Calculation API Module 11 Ready!"}


@app.post("/calculate", response_model=CalculationRead)
def create_calculation(payload: CalculationCreate, db: Session = Depends(get_db)):
    # Compute using factory
    result = CalculationFactory.compute(payload.a, payload.b, payload.type)

    calc = Calculation(
        a=payload.a,
        b=payload.b,
        type=payload.type,
        result=result
    )

    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc
