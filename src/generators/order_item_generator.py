import csv
import random


NUM_ORDER_ITEMS = 1200


def generate_order_items():

    with open("data/raw/order_items.csv",
              "w",
              newline="",
              encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "order_item_id",
            "order_id",
            "product_id",
            "quantity"
        ])

        for item_id in range(1, NUM_ORDER_ITEMS + 1):

            order_id = random.randint(100001, 100500)

            product_id = random.randint(5001, 5050)

            quantity = random.randint(1, 5)

            writer.writerow([
                item_id,
                order_id,
                product_id,
                quantity
            ])

    print("order_items.csv generated.")