import matplotlib.pyplot as plt


class Analytics:

    def price_analysis(
        self,
        df
    ):

        plt.figure(
            figsize=(8, 5)
        )

        plt.bar(
            df["name"],
            df["price"],
            color="steelblue"
        )

        plt.title(
            "Product Price Analysis"
        )

        plt.xlabel(
            "Products"
        )

        plt.ylabel(
            "Price"
        )

        plt.xticks(
            rotation=45
        )

        plt.show()

    def stock_analysis(
        self,
        df
    ):

        plt.figure(
            figsize=(8, 5)
        )

        plt.bar(
            df["name"],
            df["stock"],
            color="green"
        )

        plt.title(
            "Stock Analysis"
        )

        plt.xlabel(
            "Products"
        )

        plt.ylabel(
            "Stock Available"
        )

        plt.xticks(
            rotation=45
        )

        plt.show()

    def category_distribution(
        self,
        df
    ):

        category_count = (
            df["category"]
            .value_counts()
        )

        plt.figure(
            figsize=(7, 7)
        )

        plt.pie(
            category_count,
            labels=category_count.index,
            autopct="%1.1f%%"
        )

        plt.title(
            "Category Distribution"
        )

        plt.show()

    def shipment_trend(
        self,
        orders_df
    ):

        status_count = (
            orders_df["status"]
            .value_counts()
        )

        plt.figure(
            figsize=(8, 5)
        )

        plt.bar(
            status_count.index,
            status_count.values,
            color="orange"
        )

        plt.title(
            "Shipment Status Trend"
        )

        plt.xlabel(
            "Shipment Status"
        )

        plt.ylabel(
            "Order Count"
        )

        plt.show()