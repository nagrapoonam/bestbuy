from typing import List
from bestbuy.products import Product
"""
Store class represents a store that contains a list of products
"""
class Store:
    # initializes the store with an optional list of products. If no list is provided, an empty list is assigned
    def __init__(self, products: List[Product] = None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product): #adds a product to the store's list of products
        self.products.append(product)

    def remove_product(self, product: Product): #removes a product from the store's list of products, if it exists
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int: #calculates and returns the total quantity of all products in the store
        total_quantity = sum(product.get_quantity() for product in self.products)
        return total_quantity

    def get_all_products(self) -> List[Product]: #retrieves and returns a list of all active products in the store
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    def order(self, shopping_list: List[tuple]) -> float: #takes a shopping list and returns the total price of the order
        total_price = 0
        for product, quantity in shopping_list:
            try:
                # Apply promotion if it exists
                if product.has_promotion():
                    price = product.get_promotion().apply_promotion(product, quantity)
                else:
                    price = product.price * quantity
                total_price += price
            except Exception as e:
                print(f"Error placing order: {str(e)}")
        return total_price
