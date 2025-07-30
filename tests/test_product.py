from src.product import Product


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
