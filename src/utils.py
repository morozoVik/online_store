import json
from pathlib import Path

from .models import Category, Product


def load_categories_from_json(file_path: str | Path) -> list[Category]:
    """Загружает категории и товары из JSON файла"""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for category_data in data:
        products = [
            Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            for product_data in category_data["products"]
        ]
        categories.append(
            Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
        )

    return categories
