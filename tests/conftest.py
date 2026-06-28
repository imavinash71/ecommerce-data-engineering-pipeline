import pandas as pd
import pytest


@pytest.fixture
def sample_customer_df():

    return pd.DataFrame({

        "customer_id": [1001, 1002],

        "first_name": ["Avinash", "Rahul"],

        "last_name": ["Patil", "Sharma"],

        "email": [
            "avinash@test.com",
            "rahul@test.com"
        ],

        "phone": [
            "9876543210",
            "9876543211"
        ],

        "city": [
            " Pune ",
            " Mumbai "
        ],

        "state": [
            " Maharashtra ",
            " Maharashtra "
        ],

        "country": [
            " India ",
            " India "
        ],

        "registration_date": [
            "2025-01-01",
            "2025-02-01"
        ]

    })