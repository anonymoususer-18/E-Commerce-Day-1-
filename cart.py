import numpy as np


class CartService:

    def __init__(self):

        self.items = []

    def add_item(
        self,
        product
    ):

        self.items.append(
            product
        )

    def view_cart(
        self
    ):

        return self.items

    def calculate_total(
        self
    ):

        prices = [

            item["price"]

            for item

            in self.items

        ]

        return float(
            np.sum(prices)
        )

    def clear_cart(
        self
    ):

        self.items.clear()