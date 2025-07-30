from src.category import Category
from src.product import Product


def test_category_creation() -> None:
    """Тест создания категории."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    category = Category("Электроника", "Техника", [product])

    assert category.name == "Электроника"
    assert len(category.products.split("\n")) == 1


def test_add_product() -> None:
    """Тест добавления продукта в категорию."""
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [product1])

    category.add_product(product2)
    assert len(category.products.split("\n")) == 2


def test_category_str() -> None:
    """Тестирование строкового представления категории."""
    product = Product("Тест", "Описание", 100.0, 10)
    category = Category("Тест", "Описание", [product])
    assert str(category) == "Тест, количество продуктов: 1 шт."
