import pandas as pd
import pytest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "cars24-car-price-cleaned-new.csv"
MODEL_PATH = ROOT / "models" / "xgb_car_price_model.pkl"
print(ROOT)
print(DATA_PATH)
print(DATA_PATH.exists())

FEATURE_COLUMNS = ['km_driven', 'mileage', 'age', 'Petrol', 'Diesel', 'Electric']
TARGET_COLUMN = 'selling_price'
print(TARGET_COLUMN)
@pytest .fixture (scope = "module")
def car_data():
    """
    Fixture to load the car data from the CSV file.
    """
    return pd.read_csv(DATA_PATH)

def test_data_car_empty(car_data):
    """
    Test to check if the car data is not empty.
    """
    assert not car_data.empty, "Car data should not be empty."

def test_required_columns(car_data):
    """
    Test to check if the required columns are present in the car data.
    """
    for column in FEATURE_COLUMNS + [TARGET_COLUMN]:
        assert column in car_data.columns, f"Column '{column}' is missing from the car data."

def test_no_missing_values(car_data):

    """
    Test to check if there are no missing values in the car data.
    """
    assert not car_data.isnull().values.any(), "Car data should not contain missing values."

def test_km_driven_positive(car_data):
    """
    Test to check if the 'km_driven' column has only positive values.
    """
    assert (car_data['km_driven'] >= 0).all(), "'km_driven' should have only positive values."

def test_columns_binary(car_data):
    """
    Test to check if the 'Petrol', 'Diesel', and 'Electric' columns are binary (0 or 1).
    """
    for column in ['Petrol', 'Diesel', 'Electric']:
        assert set(car_data[column].unique()).issubset({0, 1}), f"Column '{column}' should be binary (0 or 1)."