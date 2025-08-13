from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> Any:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass


class ProductLogger:
    """Миксин для логирования создания объектов."""

    def __post_init__(self) -> None:
        """Логирует создание объекта."""
        params = {
            "name": getattr(self, "name", "unknown"),
            "description": getattr(self, "description", "unknown"),
            "price": getattr(self, "price", 0.0),
            "quantity": getattr(self, "quantity", 0),
        }
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {params}")


class Product(ProductLogger, BaseProduct):
    """Базовый класс для представления товара в магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.__post_init__()

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создает новый продукт из словаря с данными."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену продукта с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Складывает продукты по формуле: цена * количество для каждого продукта."""
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного класса")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Класс для представления смартфонов в магазине."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует экземпляр класса Smartphone."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы в магазине."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        """Инициализирует экземпляр класса LawnGrass."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
