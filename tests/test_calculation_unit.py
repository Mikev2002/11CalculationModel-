import pytest
from app.services.calculation_factory import CalculationFactory
from app.schemas.calculation import CalculationCreate


# ---------- Factory Tests ----------

def test_factory_add():
    assert CalculationFactory.compute(5, 3, "Add") == 8


def test_factory_sub():
    assert CalculationFactory.compute(10, 3, "Sub") == 7


def test_factory_multiply():
    assert CalculationFactory.compute(4, 2, "Multiply") == 8


def test_factory_divide():
    assert CalculationFactory.compute(9, 3, "Divide") == 3


def test_factory_divide_by_zero():
    with pytest.raises(ValueError):
        CalculationFactory.compute(5, 0, "Divide")


def test_factory_invalid_type():
    with pytest.raises(ValueError):
        CalculationFactory.compute(3, 3, "WrongType")


# ---------- Pydantic Schema Tests ----------

def test_schema_invalid_type():
    with pytest.raises(ValueError):
        CalculationCreate(a=1, b=2, type="BadType")


def test_schema_zero_division_validation():
    with pytest.raises(ValueError):
        CalculationCreate(a=5, b=0, type="Divide")
