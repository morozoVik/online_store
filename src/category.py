from typing import List

from src.product import Product


class Category:
    """Класс для представления категорий товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию с проверкой типа."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку с перечнем товаров."""
        return "\n".join(str(product) for product in self.__products)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."
