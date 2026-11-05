class CatalogService:

    def __init__(
        self,
        product_service
    ):

        self.product_service = (
            product_service
        )

    def search_by_category(
        self,
        category
    ):

        df = (
            self.product_service
            .get_all_products()
        )

        return df[
            df["category"]
            .str.lower()
            ==
            category.lower()
        ]

    def search_by_name(
        self,
        product_name
    ):

        df = (
            self.product_service
            .get_all_products()
        )

        return df[
            df["name"]
            .str.contains(
                product_name,
                case=False
            )
        ]