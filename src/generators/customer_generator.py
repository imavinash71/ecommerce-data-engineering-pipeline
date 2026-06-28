import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker("en_IN")

START_CUTSOMER_ID = 1001
NUM_CUSTOMERS = 100
    
CITY_STATE = {
    "Pune": "Maharashtra",
    "Mumbai": "Maharashtra",
    "Nagpur": "Maharashtra",
    "Nashik": "Maharashtra",
    "Bengaluru": "Karnataka",
    "Hyderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Delhi": "Delhi"
}


def generate_customers():
    with open("data/raw/customers.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "customer_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "city",
            "state",
            "country",
            "registration_date"
            
        ])

        for customer_id in range(START_CUTSOMER_ID, START_CUTSOMER_ID+NUM_CUSTOMERS):

            first_name = fake.first_name()
            last_name = fake.last_name()
            city = random.choice(list(CITY_STATE.keys()))
            state = CITY_STATE[city]

            email = f"{first_name.lower()}.{last_name.lower()}{customer_id}@shopsphere.com"

            phone = fake.numerify("##########")

            days_ago = random.randint(1,365)

            registration_date = (
                datetime.now() - timedelta(days=days_ago)
            ).strftime("%Y-%m-%d")

            writer.writerow([
                customer_id,
                first_name,
                last_name,
                email,
                phone,
                city,
                state,
                "India",
                registration_date,

            ])
    print("customers.csv generated successfully!")


