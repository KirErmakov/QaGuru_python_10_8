import pytest


class TestProducts:

    def test_product_check_quantity(self, product):
        assert product.check_quantity(500)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        origin_quantity = product.quantity
        quantity_to_buy = 999

        product.buy(quantity_to_buy)
        assert product.quantity == origin_quantity - quantity_to_buy

        product.buy(product.quantity)
        assert not product.quantity

    def test_product_buy_more_than_available(self, product):
        not_available_quantity = product.quantity + 1
        with pytest.raises(ValueError):
            product.buy(not_available_quantity)


class TestCart:

    def test_add_product_to_cart(self, cart, product):
        buy_count_1, buy_count_2 = 10, 5

        cart.add_product(product, buy_count_1)
        assert product in cart.products
        assert cart.products[product] == buy_count_1

        cart.add_product(product, buy_count_2)
        assert cart.products[product] == buy_count_1 + buy_count_2

    def test_add_product_more_than_available(self, cart, product):
        not_available_quantity = product.quantity + 10
        with pytest.raises(ValueError):
            cart.add_product(product, not_available_quantity)

    def test_remove_items_from_cart(self, product, fill_cart):
        fill_cart.remove_product(product, 9)

        assert product in fill_cart.products
        assert fill_cart.products[product] == 1

        fill_cart.remove_product(product, 1)
        assert product not in fill_cart.products

    def test_remove_product_from_cart(self, product, fill_cart):
        fill_cart.remove_product(product)
        assert not fill_cart.products

    def test_clear_cart(self, product, fill_cart):
        fill_cart.clear()
        assert not fill_cart.products

    def test_get_total_price(self, product, fill_cart):
        expected_total_price = product.price * fill_cart.products[product]
        assert fill_cart.get_total_price() == expected_total_price

    def test_buy_product_in_cart(self, product, fill_cart):
        fill_cart.buy()
        assert product.quantity == 990
        assert not fill_cart.products
