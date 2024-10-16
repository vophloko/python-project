# Python Project - Game Store Application

* ✓ DONE - programowanie strukturalne (tworzenie i wykorzystanie funkcji)
* ✓ DONE - programowanie obiektowe (tworzenie i użycie klas)
* ✓ DONE - regex
* ✓ DONE - json - umiejętność wczytania jsona do struktury danych i zapisania struktury do jsona
* ✓ DONE - list comprehension
* ✓ DONE - funkcje lambda
* ✓ DONE - generatory
* ✓ DONE - dekoratory


This project is a simple Game Store application developed in Python 3.12, designed to demonstrate core programming skills and fulfill the requirements of a university course. This project uses matplotlib, so please refer to installation guide.

### Project Structure
The application consists of the following core components:

* **`products.py`** - Defines the `Game` model.
* **`store.py`** - Contains the `StoreManager` class, responsible for managing the game registry.
* **`sales.py`** - Implements the `SalesManager` class, which handles sales transactions, tracks sales data, and displays the summary of purchases.
* **`main.py`** - Serves as the main entry point for the application.

### Prerequisites
- Python 3.12 is required to run this application. You can check your current Python version by running:
  ```sh
  python --version
  ```
- Run the following command to install depenencies:
  ```sh
  pip install -r requirements.txt
  ```
- Make sure that tkinter is installed on your system

### Usage
To start the application, simply run the following command from the project directory:
```sh
python ./main.py
```