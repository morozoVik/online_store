from pathlib import Path
from typing import List

import pytest

from src.models import Category
from src.utils import load_categories_from_json


@pytest.fixture
def sample_json_file(tmp_path: Path) -> Path:
    """Фикстура для создания временного JSON файла с тестовыми данными."""
    json_data = """
    [
        {
            "name": "Тест категория",
            "description": "Тестовое описание категории",
            "products": [
                {
                    "name": "Тестовый товар 1",
                    "description": "Описание тестового товара 1",
                    "price": 100.0,
                    "quantity": 5
                },
                {
                    "name": "Тестовый товар 2",
                    "description": "Описание тестового товара 2",
                    "price": 200.0,
                    "quantity": 3
                }
            ]
        }
    ]
    """
    test_file = tmp_path / "test_products.json"
    test_file.write_text(json_data, encoding="utf-8")
    return test_file


def test_load_categories_from_json(sample_json_file: Path) -> None:
    """Тестирование корректности загрузки категорий из JSON файла."""
    # Act
    categories: List[Category] = load_categories_from_json(sample_json_file)

    # Assert
    assert len(categories) == 1, "Должна быть загружена ровно одна категория"

    category = categories[0]
    assert isinstance(category, Category), "Объект должен быть экземпляром Category"
    assert category.name == "Тест категория", "Название категории не совпадает"
    assert category.description == "Тестовое описание категории", "Описание категории не совпадает"

    # Проверка товаров
    products_str = category.products
    assert isinstance(products_str, str), "Метод products должен возвращать строку"
    assert "Тестовый товар 1, 100.0 руб. Остаток: 5 шт." in products_str
    assert "Тестовый товар 2, 200.0 руб. Остаток: 3 шт." in products_str
    assert products_str.count("\n") == 1, "Должна быть одна строка между товарами"
