from user import UserService
from products import ProductService
from catalog import CatalogService
from cart import CartService
from shipping import ShippingService
from analytics import Analytics


# ==========================
# INITIALIZE SERVICES
# ==========================

user_service = UserService()

product_service = ProductService()

catalog_service = CatalogService(
    product_service
)

cart_service = CartService()

shipping_service = ShippingService()

analytics = Analytics()


# ==========================
# LOGIN / REGISTER
# ==========================

logged_in_user = None

while True:

    print("\n===== USER MENU =====")

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input(
        "\nEnter Choice: "
    )

    if choice == "1":

        user_id = int(
            input(
                "Enter User ID: "
            )
        )

        name = input(
            "Enter Name: "
        )

        username = input(
            "Enter Username: "
        )

        password = input(
            "Enter Password: "
        )

        user_service.register_user(
            user_id,
            name,
            username,
            password
        )

    elif choice == "2":

        username = input(
            "Enter Username: "
        )

        password = input(
            "Enter Password: "
        )

        user = user_service.login(
            username,
            password
        )

        if user:

            logged_in_user = user

            print(
                f"\nWelcome {user['name']}"
            )

            break

        else:

            print(
                "Invalid Credentials"
            )

    elif choice == "3":

        print(
            "Thank You"
        )

        exit()

    else:

        print(
            "Invalid Choice"
        )


# ==========================
# ECOMMERCE MENU
# ==========================

while True:

    print("\n")
    print("===================================")
    print("       E-COMMERCE SYSTEM")
    print("===================================")

    print("1. My Profile")
    print("2. View Products")
    print("3. Search By Category")
    print("4. Search By Product Name")
    print("5. Add Product To Cart")
    print("6. View Cart")
    print("7. Checkout")
    print("8. My Orders")
    print("9. Track Shipment")
    print("10. Shipping Policy")
    print("11. Product Price Analysis")
    print("12. Stock Analysis")
    print("13. Category Distribution")
    print("14. Shipment Trend")
    print("15. Logout")

    choice = input(
        "\nEnter Choice: "
    )

    # ==========================
    # PROFILE
    # ==========================

    if choice == "1":

        print(
            "\n===== PROFILE ====="
        )

        print(
            "User ID :",
            logged_in_user["user_id"]
        )

        print(
            "Name :",
            logged_in_user["name"]
        )

        print(
            "Username :",
            logged_in_user["username"]
        )

    # ==========================
    # VIEW PRODUCTS
    # ==========================

    elif choice == "2":

        print(
            "\n===== PRODUCTS ====="
        )

        print(
            product_service
            .get_all_products()
        )

    # ==========================
    # SEARCH CATEGORY
    # ==========================

    elif choice == "3":

        category = input(
            "Enter Category: "
        )

        result = (
            catalog_service
            .search_by_category(
                category
            )
        )

        if result.empty:

            print(
                "No Products Found"
            )

        else:

            print(result)

    # ==========================
    # SEARCH PRODUCT
    # ==========================

    elif choice == "4":

        name = input(
            "Enter Product Name: "
        )

        result = (
            catalog_service
            .search_by_name(
                name
            )
        )

        if result.empty:

            print(
                "No Product Found"
            )

        else:

            print(result)

    # ==========================
    # ADD TO CART
    # ==========================

    elif choice == "5":

        try:

            product_id = int(
                input(
                    "Enter Product ID: "
                )
            )

            product = (
                product_service
                .get_product(
                    product_id
                )
            )

            if product:

                cart_service.add_item(
                    product
                )

                print(
                    f"{product['name']} added to cart"
                )

            else:

                print(
                    "Product Not Found"
                )

        except ValueError:

            print(
                "Invalid Product ID"
            )

    # ==========================
    # VIEW CART
    # ==========================

    elif choice == "6":

        cart = (
            cart_service
            .view_cart()
        )

        if len(cart) == 0:

            print(
                "Cart Is Empty"
            )

        else:

            print(
                "\n===== CART ====="
            )

            for item in cart:

                print(
                    item["id"],
                    item["name"],
                    f"₹{item['price']}"
                )

            print(
                "\nTotal = ₹",
                cart_service
                .calculate_total()
            )

    # ==========================
    # CHECKOUT
    # ==========================

    elif choice == "7":

        cart = (
            cart_service
            .view_cart()
        )

        if len(cart) == 0:

            print(
                "Cart Is Empty"
            )

        else:

            total = (
                cart_service
                .calculate_total()
            )

            shipping = (
                shipping_service
                .calculate_shipping(
                    total
                )
            )

            grand_total = (
                total + shipping
            )

            print(
                "\n===== ORDER SUMMARY ====="
            )

            print(
                "Product Total : ₹",
                total
            )

            print(
                "Shipping Cost : ₹",
                shipping
            )

            print(
                "Grand Total : ₹",
                grand_total
            )

            # SAVE EACH CART ITEM AS ORDER

            for item in cart:

                user_service.add_order(
                    logged_in_user[
                        "user_id"
                    ],
                    item["name"],
                    item["price"],
                    "Processing"
                )

            print(
                "\nOrder Placed Successfully"
            )

            print(
                "Order Added To Order History"
            )

            cart_service.clear_cart()

    # ==========================
    # MY ORDERS
    # ==========================

    elif choice == "8":

        orders = (
            user_service
            .get_orders(
                logged_in_user[
                    "user_id"
                ]
            )
        )

        print(
            "\n===== MY ORDERS ====="
        )

        if orders.empty:

            print(
                "No Orders Found"
            )

        else:

            print(orders)

    # ==========================
    # TRACK SHIPMENT
    # ==========================

    elif choice == "9":

        shipment = (
            user_service
            .track_shipments(
                logged_in_user[
                    "user_id"
                ]
            )
        )

        print(
            "\n===== SHIPMENT STATUS ====="
        )

        if shipment.empty:

            print(
                "No Shipment Data Available"
            )

        else:

            print(shipment)

    # ==========================
    # SHIPPING POLICY
    # ==========================

    elif choice == "10":

        shipping_service.shipping_policy()

    # ==========================
    # ANALYTICS
    # ==========================

    elif choice == "11":

        analytics.price_analysis(
            product_service
            .get_all_products()
        )

    elif choice == "12":

        analytics.stock_analysis(
            product_service
            .get_all_products()
        )

    elif choice == "13":

        analytics.category_distribution(
            product_service
            .get_all_products()
        )

    elif choice == "14":

        analytics.shipment_trend(
            user_service.orders
        )

    # ==========================
    # LOGOUT
    # ==========================

    elif choice == "15":

        print(
            "\nLogged Out Successfully"
        )

        break

    else:

        print(
            "Invalid Choice"
        )