import pytest
from .models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


@pytest.fixture
def fill_cart(product):
    cart = Cart()
    cart.add_product(product, 10)
    return cart
