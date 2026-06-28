from generators.customer_generator import generate_customers
from generators.product_generator import generate_products
from generators.order_generator import generate_orders
from generators.order_item_generator import generate_order_items


def main():

    print("Generating datasets...\n")

    generate_customers()

    generate_products()

    generate_orders()

    generate_order_items()

    print("\nAll datasets generated successfully.")


# if __name__ == "__main__":
#     main()