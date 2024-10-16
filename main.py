from products import Game
from store import StoreManager
from sales import SalesManager
from random import randint

from utilities import print_header


def simulate_adding_products(store_manager):
    """
    Simulates a scenario where an administrator of the online store
    wants to add new products and list results in a specific way.
    """
    store_manager.import_from_json("games_to_import.json")
    store_manager.add_product(
        Game(
            name="The Talos Principle",
            price=39.99,
            genre=["Puzzle", "Adventure"],
            developer="Croteam",
            publisher="Devolver Digital",
            release_date="2014/12/11",
        )
    )
    store_manager.list_products(
        lambda product: product.price > 30 and product.price < 40,
        lambda product: product.price,
        reverse=True,
        verbose=False,  # Suppress printing the results
    )
    store_manager.list_products(
        lambda product: product.name.startswith("The"),
        lambda product: product.name,
        verbose=False,
    )
    # Normally it would export it to the same file to keep data in sync...
    store_manager.export_to_json("exported_games.json")


def simulate_setting_discounts(sales_manager):
    discounts = [
        ("Bastion", 20),
        ("Celeste", 75),
        ("Chrono Trigger", 90),
        ("Okami", 50),
    ]

    for name, percentage in discounts:
        sales_manager.discount_manager.add_discount(name, percentage)


def simulate_sales(store_manager, sales_manager):
    products = (
        product
        for product in store_manager.get_products().values()
        for _ in range(randint(1000, 10000))
    )

    for product in products:
        sales_manager.process_sale(product.name)


def print_available_commands():
    commands = [
        ("list", "list registered products"),
        ("buy <product name>", "register a sale"),
        ("discounts", "list discounted products"),
        ("summary", "summarize sales"),
        ("graph", "summarize sales as graph"),
        ("exit", "exit the program"),
    ]

    print("\nAvailable commands:")
    for command, description in commands:
        print(f"\t{command:20} - {description}")


if __name__ == "__main__":
    print_header("Welcome to the online store!")
    store_manager = StoreManager()
    sales_manager = SalesManager(store_manager)

    simulate_adding_products(store_manager)
    simulate_setting_discounts(sales_manager)
    simulate_sales(store_manager, sales_manager)

    while True:
        print_available_commands()
        print("\n> ", end="")
        user_input = input().strip()
        if user_input == "exit":
            break
        elif user_input == "discounts":
            sales_manager.list_discounted_products()
        elif user_input == "list":
            print_header("Registered Products")
            print(
                *[product for product in store_manager.get_products().keys()], sep="\n"
            )
        elif user_input == "summary":
            sales_manager.summarize_sales()
        elif user_input == "graph":
            sales_manager.summarize_sales_as_graph()
        elif user_input.startswith("buy "):
            product_name = user_input[4:]
            if product_name in store_manager.get_products():
                sales_manager.process_sale(product_name)
                print("Sale registered successfully")
            else:
                print(
                    f"{product_name} is not available in the store. Please enter an exact product name."
                )
        else:
            print("Invalid input. Please try again.")
