"""
'Product' class that represents a product with its name, price, and quantity
"""
class Product:
    # initializing the product with a name, price, and quantity and setting the product active by default.
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if price <= 0:
            raise ValueError("Price must be greater than zero")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def has_promotion(self):
        return self.promotion is not None

    def show(self):
        if self.promotion:
            promotion_name = self.promotion.name
        else:
            promotion_name = "No promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {promotion_name}"

    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is not active")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise Exception("Insufficient quantity available")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        if self.promotion:
            promotion_name = self.promotion.name
        else:
            promotion_name = "No promotion"
        return f"{self.name} (Non-Stocked Product), Price: {self.price}, Promotion: {promotion_name}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity_limit):
        super().__init__(name, price, quantity=quantity_limit)

    def show(self):
        if self.promotion:
            promotion_name = self.promotion.name
        else:
            promotion_name = "No promotion"
        return f"{self.name} (Limited Product), Price: {self.price}, Quantity Limit: {self.quantity}, Promotion: {promotion_name}"
