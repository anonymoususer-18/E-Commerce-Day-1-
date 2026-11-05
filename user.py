import pandas as pd


class UserService:

    def __init__(self):

        self.users = pd.read_csv(
            "users.csv"
        )

        self.orders = pd.read_csv(
            "orders.csv"
        )

    def register_user(
        self,
        user_id,
        name,
        username,
        password
    ):

        new_user = pd.DataFrame([
            {
                "user_id": user_id,
                "name": name,
                "username": username,
                "password": password
            }
        ])

        self.users = pd.concat(
            [self.users, new_user],
            ignore_index=True
        )

        self.users.to_csv(
            "users.csv",
            index=False
        )

        print(
            "User Registered Successfully"
        )

    def login(
        self,
        username,
        password
    ):

        user = self.users[
            (
                self.users["username"]
                == username
            )
            &
            (
                self.users["password"]
                == password
            )
        ]

        if user.empty:

            return None

        return (
            user.iloc[0]
            .to_dict()
        )

    def get_orders(
        self,
        user_id
    ):

        return self.orders[
            self.orders["user_id"]
            == user_id
        ]

    def track_shipments(
        self,
        user_id
    ):

        return self.orders[
            self.orders["user_id"]
            == user_id
        ][
            [
                "order_id",
                "product",
                "status"
            ]
        ]

    # NEW METHOD

    def add_order(
        self,
        user_id,
        product,
        total,
        status="Processing"
    ):

        if len(self.orders) == 0:

            order_id = 1001

        else:

            order_id = (
                self.orders["order_id"]
                .max()
                + 1
            )

        new_order = pd.DataFrame([
            {
                "order_id": order_id,
                "user_id": user_id,
                "product": product,
                "total": total,
                "status": status
            }
        ])

        self.orders = pd.concat(
            [
                self.orders,
                new_order
            ],
            ignore_index=True
        )

        self.orders.to_csv(
            "orders.csv",
            index=False
        )