import csv
import random

START_PRODUCT_ID = 5001
NUM_PRODUCTS = 50

PRODUCT_CATALOG = {
    "Electronics": {
        "Apple": [("iPhone 15", 79999), ("MacBook Air", 99999)],
        "Samsung": [("Galaxy S24", 74999), ("Galaxy Tab", 42999)],
        "Dell": [("Inspiron", 55999), ("XPS 13", 109999)]
    },
    "Fashion": {
        "Nike": [("Running Shoes", 4999), ("T-Shirt", 1499)],
        "Adidas": [("Sneakers", 5999), ("Jacket", 3499)]
    },
    "Home": {
        "IKEA": [("Chair", 2999), ("Table", 7999)],
        "Philips": [("LED Lamp", 1999)]
    }
}


def generate_products():

    with open("data/raw/products.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "product_id",
            "product_name",
            "category",
            "brand",
            "price",
            "stock_quantity"
        ])

        for product_id in range(START_PRODUCT_ID,
                                START_PRODUCT_ID + NUM_PRODUCTS):

            category = random.choice(list(PRODUCT_CATALOG.keys()))

            brand = random.choice(
                list(PRODUCT_CATALOG[category].keys())
            )

            product_name, price = random.choice(
                PRODUCT_CATALOG[category][brand]
            )

            stock = random.randint(10, 500)

            writer.writerow([
                product_id,
                product_name,
                category,
                brand,
                price,
                stock
            ])

    print("products.csv generated.")