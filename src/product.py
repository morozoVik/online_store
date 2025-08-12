from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод инициализации продукта."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления продукта."""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> Any:
        """Абстрактный метод сложения продуктов."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер для цены продукта."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Абстрактный сеттер для цены продукта."""
        pass


class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализирует миксин и логирует создание объекта."""
        super().__init__(*args, **kwargs)
        class_name = self.__class__.__name__
        params = ", ".join([f"{k}={v!r}" for k, v in kwargs.items()])
        print(f"Создан объект класса {class_name} с параметрами: {params}")

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        class_name = self.__class__.__name__
        params = ", ".join([f"{k}={v!r}" for k, v in self.__dict__.items()])
        return f"{class_name}({params})"


class Product(LoggingMixin, BaseProduct):
    """Базовый класс для представления товара в магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализирует экземпляр класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name=name, description=description, price=price, quantity=quantity)

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
