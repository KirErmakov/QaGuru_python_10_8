from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity

    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    products: dict[Product, int]

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        if product not in self.products:
            raise ValueError(f"В корзине отсутствуют товары для удаления")
        elif remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        return sum(product.price * quantity for product, quantity in self.products.items())

    def buy(self):
        for product, quantity in self.products.items():
            if not product.check_quantity(quantity):
                raise ValueError(f"Недостаточно товара {product.name} на складе")
            product.buy(quantity)
        self.clear()
