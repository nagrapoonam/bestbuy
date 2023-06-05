"""
Promotion classes for the store
"""

from abc import ABC, abstractmethod
from bestbuy.products import Product


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        # Only apply the promotion if the product matches
        if isinstance(product, Product) and product.name == "MacBook Air M2":
            # Calculate the discounted price
            num_pairs = quantity // 2
            num_single = quantity % 2
            total_price = (num_pairs * product.price + num_single * product.price / 2)
            return total_price
        else:
            # No promotion applied, return original price
            return product.price * quantity

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        # Only apply the promotion if the product matches
        if isinstance(product, Product) and product.name == "Bose QuietComfort Earbuds":
            # Calculate the discounted price
            num_groups = quantity // 3
            num_single = quantity % 3
            total_price = (num_groups * 2 * product.price + num_single * product.price)
            return total_price
        else:
            # No promotion applied, return original price
            return product.price * quantity

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        # Calculate the discounted price
        discount = self.percent / 100
        total_price = product.price * quantity * (1 - discount)
        return total_price
