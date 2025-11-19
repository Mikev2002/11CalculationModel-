from pydantic import BaseModel, Field, field_validator
from typing import Optional


class CalculationCreate(BaseModel):
    a: float
    b: float
    type: str = Field(..., description="Add, Sub, Multiply, Divide")

    @field_validator("type")
    @classmethod
    def validate_type(cls, v):
        allowed = {"Add", "Sub", "Multiply", "Divide"}
        if v not in allowed:
            raise ValueError("Invalid calculation type. Must be Add, Sub, Multiply, Divide")
        return v

    @field_validator("b")
    @classmethod
    def validate_division(cls, v, values):
        if "type" in values and values["type"] == "Divide" and v == 0:
            raise ValueError("Cannot divide by zero")
        return v


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: str
    result: Optional[float]

    model_config = {
        "from_attributes": True
    }


