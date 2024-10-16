from datetime import datetime
from utilities import print_header, print_subheader
import matplotlib.pyplot as plt


class SalesHistoryTracker:
    def __init__(self):
        self._sales_history = []

    def track_sale(self, product, price):
        if not product:
            raise ValueError("No product specified")
        self._sales_history.append(
            {
                "product": product,
                "time_of_purchase": datetime.now(),
                "price": price,
            }
        )

    def print_track_sales_history(self):
        print_header("Sales History")
        for record in self._sales_history:
            print(
                f"{record['time_of_purchase']:%Y-%m-%d %H:%M:%S} {record['product'].name} - {record['price']:.2f}"
            )


class DiscountManager:
    def __init__(self):
        self._discounted_products = {}

    def add_discount(self, product_name, discount_percentage):
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        if product_name in self._discounted_products:
            raise ValueError(f"Discount for {product_name!r} already added")
        self._discounted_products[product_name] = discount_percentage

    def remove_discount(self, product_name):
        if product_name not in self._discounted_products:
            raise ValueError(f"Discount for {product_name!r} not found")
        del self._discounted_products[product_name]

    def list_discounted_products(self):
        print_header("Discounted Products")
        for product_name, discount_percentage in self._discounted_products.items():
            print(f"{product_name!r}: {discount_percentage}%")


class SalesManager:
    def __init__(self, store_manager):
        self.store_manager = store_manager
        self.sales_history_tracker = SalesHistoryTracker()
        self.discount_manager = DiscountManager()

    def process_sale(self, product_name):
        product = self.store_manager.get_product(product_name)
        if product is None:
            raise ValueError(f"Product {product_name!r} not found")

        discount_percentage = self.discount_manager._discounted_products.get(
            product_name
        )
        price = product.price
        if discount_percentage is not None:
            price -= price * discount_percentage / 100

        self.sales_history_tracker.track_sale(product, price)

    def print_track_sales_history(self):
        self.sales_history_tracker.print_track_sales_history()

    def list_discounted_products(self):
        self.discount_manager.list_discounted_products()

    def summarize_sales_as_graph(self):
        product_name, _, earned = zip(*self._generate_sales_summary())
        plt.bar(product_name, earned, label="Revenue")
        plt.title("Sales Summary")
        plt.xlabel("Product")
        plt.ylabel("Revenue")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.legend()
        plt.show()

    def summarize_sales(self):
        print_header("Sales Summary")
        total_earned = 0
        for product_name, count, earned in self._generate_sales_summary():
            total_earned += earned
            print(f"{product_name!r:<66}{count:>10}{earned:>24.2f}")
        print_subheader(f"Total revenue: {total_earned:.2f}")

    def _generate_sales_summary(self):
        products = self.store_manager.get_products()
        sales = self.sales_history_tracker._sales_history
        for product in products.values():
            earned = sum(sale["price"] for sale in sales if sale["product"] is product)
            count = sum(1 for sale in sales if sale["product"] is product)
            yield product.name, count, earned
