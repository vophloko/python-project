from products import Game
from store import StoreManager
from sales import SalesManager
from random import randint

if __name__ == "__main__":
    store_manager = StoreManager()
    sales_manager = SalesManager(store_manager)

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
        lambda product: product.price < 15, sort_key=lambda product: product.price
    )
    store_manager.list_products(
        lambda product: product.name.startswith("The"),
        sort_key=lambda product: product.name,
    )

    store_manager.export_to_json("exported_games.json")

    sales_manager.discount_manager.add_discount("Bastion", 20)
    sales_manager.discount_manager.add_discount("Okami", 50)
    sales_manager.discount_manager.add_discount("Chrono Trigger", 90)

    products = (
        product
        for product in store_manager.get_products().values()
        for _ in range(randint(1000, 10000))
    )

    for product in products:
        sales_manager.process_sale(product.name)

    sales_manager.list_discounted_products()
    sales_manager.summarize_sales()
