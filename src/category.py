from typing import List, Union

from src.product import LawnGrass, Product, Smartphone


class Category:
    """Класс для представления категорий товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Union[Product, Smartphone, LawnGrass]]) -> None:
        """Инициализирует экземпляр класса Category."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Union[Product, Smartphone, LawnGrass]) -> None:
        """Добавляет продукт в категорию с проверкой типа."""
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только объекты классов Product, Smartphone или LawnGrass")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку с перечнем товаров."""
        return "\n".join(str(product) for product in self.__products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
