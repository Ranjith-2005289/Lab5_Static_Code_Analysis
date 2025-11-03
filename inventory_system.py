"""
Inventory System Module
-----------------------
Handles adding, removing, saving, and loading items in stock.
Includes input validation, logging, and secure file handling.
"""

import json
from datetime import datetime
import ast

# Global inventory storage
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Adds an item to the stock data.

    Args:
        item (str): The name of the item.
        qty (int): Quantity to add.
        logs (list): Optional list to store log entries.

    Returns:
        None
    """
    if logs is None:
        logs = []

    # Validate input types
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types for add_item().")
        return

    # Add quantity to stock
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Removes a given quantity of an item from stock.

    Args:
        item (str): Item name to remove.
        qty (int): Quantity to remove.

    Returns:
        None
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")
    except Exception as e:
        print(f"Error removing item: {e}")


def get_qty(item):
    """
    Returns the quantity of a given item.

    Args:
        item (str): Item name.

    Returns:
        int: Quantity in stock.
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Loads stock data from a JSON file.

    Args:
        file (str): File path to load data from.

    Returns:
        None
    """
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print("Error decoding JSON file. File may be corrupted.")


def save_data(file="inventory.json"):
    """
    Saves the current stock data to a JSON file.

    Args:
        file (str): File path to save data to.

    Returns:
        None
    """
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")


def print_data():
    """
    Prints a report of all items and quantities.
    """
    print("\n=== Inventory Report ===")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")
    print("========================\n")


def check_low_items(threshold=5):
    """
    Returns a list of items below a quantity threshold.

    Args:
        threshold (int): The minimum quantity for acceptable stock.

    Returns:
        list: Items below the threshold.
    """
    result = [item for item, qty in stock_data.items() if qty < threshold]
    return result


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("grape", 12)

    remove_item("apple", 3)
    remove_item("orange", 1)  # orange not in stock, handled gracefully

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low stock items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    # Demonstration of safe evaluation (instead of eval)
    expression = "{'safe_eval_example': True}"
    safe_data = ast.literal_eval(expression)
    print("Safe eval output:", safe_data)


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
