import json
from products import Game
from errors import ImportError, ExportError
from utilities import print_header


class StoreManager:
    def __init__(self):
        self._products = {}

    def import_from_json(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            for product_data in data:
                product = self._map_data_to_product(product_data)

                try:
                    self.add_product(product)
                except ValueError as e:
                    print(f"Error creating product from JSON file: {e}")

        except FileNotFoundError as e:
            raise ImportError(f"File {filename} not found: {e}")

        except json.JSONDecodeError as e:
            raise ImportError(f"Error decoding JSON file: {e}")

    def export_to_json(self, filename):
        try:
            products_data = [
                self._map_product_to_data(product)
                for product in self._products.values()
            ]

            with open(filename, "w") as file:
                json.dump(products_data, file, indent=4)

        except IOError as e:
            raise ExportError(f"Error writing to file {filename}: {e}")

        except AttributeError as e:
            raise ExportError(f"Error exporting product to JSON file: {e}")

    def _map_data_to_product(self, product_data):
        match product_data:
            case {"type": "Game"}:
                return Game(**{key: product_data[key] for key in Game.info_attributes})
            case _:
                raise ValueError(f"Invalid product type: {product_data.get('type')}")

    def _map_product_to_data(self, product):
        match product:
            case Game():
                return {
                    "type": "Game",
                    **{key: getattr(product, key) for key in Game.info_attributes},
                }

    def add_product(self, product):
        if product.name in self._products:
            raise ValueError(f"Product {product.name!r} already exists")
        self._products[product.name] = product

    def remove_product(self, name):
        if name in self._products:
            del self._products[name]
        else:
            raise ValueError(f"Product {name!r} not found")

    def update_product(self, name, **kwargs):
        if name not in self._products:
            raise ValueError(f"Product {name!r} not found")
        product = self._products[name]

        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                raise ValueError(f"{key} is not a valid attribute of {name!r}")

    def get_product(self, name):
        return self._products.get(name)

    def get_products(self):
        return self._products

    def list_products(
        self, filter_func=None, sort_key=None, reverse=False, verbose=True
    ):
        products = list(self._products.values())

        if filter_func:
            products = list(filter(filter_func, products))

        if sort_key:
            products.sort(key=sort_key, reverse=reverse)

        if not products:
            raise ValueError("No products found")

        if verbose:
            print_header("Registered Products")
            for product in products:
                print(product)
