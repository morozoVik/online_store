from pathlib import Path

import pytest

from src.models import Category, Product
from src.utils import load_categories_from_json


@pytest.fixture
def sample_json_file(tmp_path: Path) -> Path:
    """Фикстура для создания временного JSON файла."""
    json_data = """
    [
        {
            "name": "Тест категория",
            "description": "Описание",
            "products": [
                {
                    "name": "Товар 1",
                    "description": "Описание 1",
                    "price": 100.0,
                    "quantity": 5
                }
            ]
        }
    ]
    """
    test_file = tmp_path / "test_products.json"
    test_file.write_text(json_data, encoding="utf-8")
    return test_file


def test_load_categories_from_json(sample_json_file: Path) -> None:
    """Тестирование загрузки категорий из JSON."""
    categories = load_categories_from_json(sample_json_file)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Товар 1"
