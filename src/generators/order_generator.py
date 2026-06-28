import csv
import random
from datetime import datetime, timedelta

START_ORDER_ID = 100001
NUM_ORDERS = 500

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

ORDER_STATUS = [
    "Delivered",
    "Shipped",
    "Processing",
    "Cancelled"
]


def generate_orders():

    with open("data/raw/orders.csv", "w",
              newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "order_id",
            "customer_id",
            "order_date",
            "payment_method",
            "status",
            "total_amount"
        ])

        for order_id in range(
                START_ORDER_ID,
                START_ORDER_ID + NUM_ORDERS):

            customer_id = random.randint(1001, 1100)

            order_date = (
                datetime.now()
                - timedelta(days=random.randint(1, 365))
            ).strftime("%Y-%m-%d")

            payment = random.choice(PAYMENT_METHODS)

            status = random.choice(ORDER_STATUS)

            writer.writerow([
                order_id,
                customer_id,
                order_date,
                payment,
                status,
                0
            ])

    print("orders.csv generated.")