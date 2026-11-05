import pandas as pd


class ProductService:

    def __init__(self):

        self.df = pd.read_csv(
            "products.csv"
        )

    def get_all_products(self):

        return self.df

    def get_product(
        self,
        product_id
    ):

        product = self.df[
            self.df["id"] == product_id
        ]

        if product.empty:

            return None

        return (
            product.iloc[0]
            .to_dict()
        )