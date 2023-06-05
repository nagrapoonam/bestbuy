import pytest
from bestbuy.products import Product

def test_creating_prod():
    product = Product("MacBook Pro", price=2000, quantity=10)
    assert product.name == "MacBook Pro"
    assert product.price == 2000
    assert product.quantity == 10
    assert product.is_active() is True

def test_creating_prod_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=-100, quantity=5)

def test_prod_becomes_inactive():
    product = Product("Headphones", price=50, quantity=1)
    assert product.is_active() is True
    product.set_quantity(0)
    assert product.is_active() is False

def test_buy_modifies_quantity():
    product = Product("Phone", price=500, quantity=10)
    quantity = 5
    total_price = product.buy(quantity)
    assert product.quantity == 5
    assert total_price == 2500

def test_buy_too_much():
    product = Product("Laptop", price=1000, quantity=3)
    with pytest.raises(Exception):
        product.buy(5)

