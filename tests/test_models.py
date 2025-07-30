import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product() -> Product:
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_category(sample_product: Product) -> Category:
    return Category("Test Category", "Test Description", [sample_product])


def test_product_initialization(sample_product: Product) -> None:
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_category_initialization(sample_category: Category, sample_product: Product) -> None:
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert "Test Product" in sample_category.products
    assert "100.0 руб." in sample_category.products


def test_category_count() -> None:
    initial_count = Category.category_count
    _ = Category("Temp", "Temp", [])
    assert Category.category_count == initial_count + 1


def test_product_count() -> None:
    initial_count = Category.product_count
    product1 = Product("P1", "D1", 1.0, 1)
    product2 = Product("P2", "D2", 2.0, 2)
    _ = Category("Temp", "Temp", [product1, product2])
    assert Category.product_count == initial_count + 2
