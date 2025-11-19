from pydantic import BaseModel, Field, field_validator
from typing import Optional


class CalculationCreate(BaseModel):
    a: float
    type: str = Field(..., description="Add, Sub, Multiply, Divide")
    b: float

    @field_validator("type")
    @classmethod
    def validate_type(cls, v):
        allowed = {"Add", "Sub", "Multiply", "Divide"}
        if v not in allowed:
            raise ValueError("Invalid calculation type. Must be Add, Sub, Multiply, Divide")
        return v

    @field_validator("b")
    @classmethod
    def validate_division(cls, v, info):
        # info is ValidationInfo → the actual input values validated so far are in info.data
        data = info.data or {}

        # At this point, 'type' has already been validated because it appears before 'b'
        if data.get("type") == "Divide" and v == 0:
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
