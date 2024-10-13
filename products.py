from abc import ABC
from validators import (
    validator,
    validate_name,
    validate_price,
    validate_genre,
    validate_developer,
    validate_publisher,
    validate_release_date,
)


@validator("name", validate_name)
@validator("price", validate_price)
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return (
            "\n".join(f"{key}: {value}" for key, value in self.__dict__.items()) + "\n"
        )


@validator("genre", validate_genre)
@validator("developer", validate_developer)
@validator("publisher", validate_publisher)
@validator("release_date", validate_release_date)
class Game(Product):
    info_attributes = [
        "name",
        "price",
        "genre",
        "developer",
        "publisher",
        "release_date",
    ]

    def __init__(self, name, price, genre, developer, publisher, release_date):
        super().__init__(name, price)
        self.genre = genre
        self.developer = developer
        self.publisher = publisher
        self.release_date = release_date
