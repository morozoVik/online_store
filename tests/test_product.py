import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


def test_product_creation() -> None:
    """Тест создания продукта."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_price_setter() -> None:
    """Тест сеттера цены."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    product.price = 60000.0
    assert product.price == 60000.0

    product.price = -1000.0
    assert product.price == 60000.0


def test_new_product_classmethod() -> None:
    """Тест класс-метода создания продукта."""
    product_data = {"name": "Ноутбук", "description": "Игровой ноутбук", "price": 100000.0, "quantity": 5}
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Ноутбук"


def test_product_addition() -> None:
    """Тест сложения продуктов."""
    product1 = Product("Телефон", "Смартфон", 100.0, 10)
    product2 = Product("Ноутбук", "Игровой", 200.0, 2)
    assert product1 + product2 == 1400.0


def test_product_addition_with_invalid_type() -> None:
    """Тест сложения продукта с объектом другого типа."""
    product = Product("Телефон", "Смартфон", 100.0, 10)
    with pytest.raises(TypeError):
        product + 100  # type: ignore


def test_add_product_invalid_type() -> None:
    category = Category("Тест", "Тест", [])
    with pytest.raises(TypeError):
        category.add_product("не продукт")  # type: ignore


def test_smartphone_creation() -> None:
    """Тест создания смартфона."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Флагман Apple",
        price=100000.0,
        quantity=10,
        efficiency=3.5,
        model="15 Pro",
        memory=256,
        color="Black",
    )
    assert smartphone.name == "iPhone 15"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"


def test_lawn_grass_creation() -> None:
    """Тест создания газонной травы."""
    grass = LawnGrass(
        name="Premium Grass",
        description="Мягкая газонная трава",
        price=500.0,
        quantity=100,
        country="Russia",
        germination_period=14,
        color="Green",
    )
    assert grass.name == "Premium Grass"
    assert grass.country == "Russia"
    assert grass.germination_period == 14


def test_add_different_products() -> None:
    """Тест сложения разных типов продуктов."""
    smartphone = Smartphone(
        name="iPhone", description="", price=100, quantity=1, efficiency=1, model="", memory=1, color=""
    )
    grass = LawnGrass(name="Grass", description="", price=10, quantity=1, country="", germination_period=1, color="")
    with pytest.raises(TypeError):
        smartphone + grass


def test_add_same_products() -> None:
    """Тест сложения одинаковых типов продуктов."""
    smartphone1 = Smartphone(
        name="iPhone", description="", price=100, quantity=2, efficiency=1, model="", memory=1, color=""
    )
    smartphone2 = Smartphone(
        name="Samsung", description="", price=200, quantity=3, efficiency=1, model="", memory=1, color=""
    )
    assert smartphone1 + smartphone2 == 800


def test_add_invalid_type_to_category():
    """Тест добавления неверного типа в категорию."""
    category = Category("Test", "Test", [])
    with pytest.raises(TypeError):
        category.add_product("не продукт")
