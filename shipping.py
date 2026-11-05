import numpy as np


class ShippingService:

    def calculate_shipping(
        self,
        amount
    ):

        if amount > 20000:

            return 0

        return float(

            np.round(
                amount * 0.05,
                2
            )

        )

    def shipping_policy(
        self
    ):

        print(
            "\n===== SHIPPING POLICY ====="
        )

        print(
            "Orders Above ₹20,000 : FREE"
        )

        print(
            "Orders Below ₹20,000 : 5% Charge"
        )