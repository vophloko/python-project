import re
from datetime import datetime
from enums import Genre


class Validator:
    def __init__(self, attribute_name, validation_function):
        self.attribute_name = attribute_name
        self.validation_function = validation_function

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.attribute_name)

    def __set__(self, instance, value):
        self.validation_function(value)
        instance.__dict__[self.attribute_name] = value


def validator(attribute_name, validation_function):
    def decorator(cls):
        setattr(cls, attribute_name, Validator(attribute_name, validation_function))
        return cls

    return decorator


def validate_name(name):
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    if not name or len(name) > 64:
        raise ValueError(
            "Name cannot be empty and must be no longer than 64 characters"
        )


def validate_price(price):
    if not isinstance(price, (int, float)):
        raise ValueError("Price must be a number")
    if price < 0:
        raise ValueError("Price cannot be negative")


def validate_genre(genre):
    # This could be a set comprehension. It's written as a list to fulfill the requirements of the task
    valid_genres = [genre.value for genre in Genre]
    if not set(genre).issubset(valid_genres):
        raise ValueError(f"Invalid genres: {', '.join(set(genre) - valid_genres)}")


def validate_developer(developer):
    if not isinstance(developer, str):
        raise ValueError("Developer must be a string")
    if not 2 <= len(developer) <= 64:
        raise ValueError("Developer must have 2-64 characters")
    if developer.isdigit():
        raise ValueError("Developer cannot be numeric")


def validate_publisher(publisher):
    if not isinstance(publisher, str):
        raise ValueError("Publisher must be a string")
    if not 2 <= len(publisher) <= 64:
        raise ValueError("Publisher must have 2-64 characters")
    if not re.match(r"^[A-Za-z0-9\s.]+$", publisher):
        raise ValueError(
            "Publisher cannot contain special characters except spaces and dots"
        )


def validate_release_date(release_date):
    if not re.match(r"^\d{4}/\d{2}/\d{2}$", release_date):
        raise ValueError("Release date must be in the format yyyy/mm/dd")
    try:
        datetime.strptime(release_date, "%Y/%m/%d")
    except ValueError:
        raise ValueError("Release date must be a valid date")
