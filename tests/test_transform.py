import pandas as pd

from src.etl.transform import transform_customers


def test_registration_date_is_datetime():

    df = pd.DataFrame({

        "customer_id": [1],

        "first_name": ["Avinash"],

        "last_name": ["Patil"],

        "email": ["a@test.com"],

        "phone": ["9876543210"],

        "city": [" Pune "],

        "state": [" Maharashtra "],

        "country": [" India "],

        "registration_date": ["2025-01-01"]

    })

    transformed = transform_customers(df)

    assert pd.api.types.is_datetime64_any_dtype(
        transformed["registration_date"]
    )


def test_city_spaces_removed():

    df = pd.DataFrame({

        "customer_id":[1],

        "first_name":["Avinash"],

        "last_name":["Patil"],

        "email":["a@test.com"],

        "phone":["9876543210"],

        "city":[" Pune "],

        "state":[" Maharashtra "],

        "country":[" India "],

        "registration_date":["2025-01-01"]

    })

    transformed = transform_customers(df)

    assert transformed.loc[0, "city"] == "Pune"


def test_duplicates_removed():

    df = pd.DataFrame({

        "customer_id":[1,1],

        "first_name":["Avinash","Avinash"],

        "last_name":["Patil","Patil"],

        "email":["a@test.com","a@test.com"],

        "phone":["9876543210","9876543210"],

        "city":["Pune","Pune"],

        "state":["MH","MH"],

        "country":["India","India"],

        "registration_date":[
            "2025-01-01",
            "2025-01-01"
        ]

    })

    transformed = transform_customers(df)

    assert len(transformed) == 1