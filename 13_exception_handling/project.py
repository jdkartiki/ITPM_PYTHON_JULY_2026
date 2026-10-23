# ---------------- CUSTOM EXCEPTIONS ----------------

class ProductNotFoundException(Exception):
    pass


class InvalidQuantityException(Exception):
    pass


class InsufficientStockException(Exception):
    pass


class EmptyCartException(Exception):
    pass


# ---------------- PRODUCT CLASS ----------------

class Product:

    def __init__(self, product_id, product_name, price, quantity_available):

        self.product_id = product_id
        self.product_name = product_name
        self.__price = price
        self.__quantity_available = quantity_available

    # Display product
    def display_product(self):

        print(
            self.product_id," | ",self.product_name," | ₹",self.__price," | Stock:",self.__quantity_available
        )

    # Get price
    def get_price(self):

        return self.__price

    # Get stock
    def get_stock(self):

        return self.__quantity_available

    # Update stock
    def update_stock(self, quantity):

        self.__quantity_available += quantity


# ---------------- SHOPPING CART CLASS ----------------

class ShoppingCart:

    def __init__(self):

        self.cart_items = {}

    # Add product
    def add_product(self, product, quantity):

        if quantity <= 0:
            raise InvalidQuantityException(
                "Quantity must be greater than 0."
            )

        if quantity > product.get_stock():
            raise InsufficientStockException(
                "Only "
                + str(product.get_stock())
                + " units are available."
            )

        # If product already exists
        if product.product_id in self.cart_items:

            self.cart_items[product.product_id]["quantity"] += quantity

        else:

            self.cart_items[product.product_id] = {
                "product": product,
                "quantity": quantity
            }

        # Reduce product stock
        product.update_stock(-quantity)

        print("\nProduct added to cart successfully!")

    # Remove product
    def remove_product(self, product_id):

        if product_id not in self.cart_items:

            raise ProductNotFoundException(
                "Product is not present in cart."
            )

        item = self.cart_items[product_id]

        product = item["product"]
        quantity = item["quantity"]

        # Return stock
        product.update_stock(quantity)

        del self.cart_items[product_id]

        print("\nProduct removed from cart successfully!")

    # Update quantity
    def update_quantity(self, product_id, new_quantity):

        if product_id not in self.cart_items:

            raise ProductNotFoundException(
                "Product is not present in cart."
            )

        if new_quantity <= 0:

            raise InvalidQuantityException(
                "Quantity must be greater than 0."
            )

        item = self.cart_items[product_id]

        product = item["product"]
        old_quantity = item["quantity"]

        difference = new_quantity - old_quantity

        # Increasing quantity
        if difference > 0:

            if difference > product.get_stock():

                raise InsufficientStockException(
                    "Not enough stock available."
                )

            product.update_stock(-difference)

        # Decreasing quantity
        elif difference < 0:

            product.update_stock(-difference)

        item["quantity"] = new_quantity

        print("\nCart quantity updated successfully!")

    # Calculate total
    def calculate_total(self):

        total = 0

        for item in self.cart_items.values():

            product = item["product"]
            quantity = item["quantity"]

            total += product.get_price() * quantity

        return total

    # Display cart
    def display_cart(self):

        if len(self.cart_items) == 0:

            raise EmptyCartException(
                "Cart is empty."
            )

        print("\n========== SHOPPING CART ==========")

        for item in self.cart_items.values():

            product = item["product"]
            quantity = item["quantity"]

            price = product.get_price()

            subtotal = price * quantity

            print("\nProduct ID ::", product.product_id)
            print("Product    ::", product.product_name)
            print("Price      :: ₹", price)
            print("Quantity   ::", quantity)
            print("Subtotal   :: ₹", subtotal)

        print("\n===================================")
        print("Total Amount :: ₹", self.calculate_total())

    # Checkout
    def checkout(self):

        if len(self.cart_items) == 0:

            raise EmptyCartException(
                "Cannot checkout. Cart is empty."
            )

        print("\n========== FINAL BILL ==========")

        for item in self.cart_items.values():

            product = item["product"]
            quantity = item["quantity"]

            price = product.get_price()
            subtotal = price * quantity

            print(product.product_name,"x",quantity," = ₹",subtotal)

        total = self.calculate_total()

        print("--------------------------------")
        print("Total Amount :: ₹", total)
        print("Order placed successfully!")
        print("Thank you for shopping with us!")

        # Empty cart after checkout
        self.cart_items.clear()


# ---------------- FIND PRODUCT ----------------

def find_product(products, product_id):

    for product in products:

        if product.product_id == product_id:

            return product

    raise ProductNotFoundException(
        "Product ID does not exist."
    )


# ---------------- MAIN PROGRAM ----------------

products = [

    Product(101, "Wireless Mouse", 799, 5),
    Product(102, "Keyboard", 1299, 10),
    Product(103, "USB Cable", 299, 15),
    Product(104, "Headphones", 1999, 8),
    Product(105, "Laptop Stand", 1499, 6)
]


cart = ShoppingCart()


while True:

    print("\n")
    print("========== ONLINE SHOPPING SYSTEM ==========")
    print("1. Display Products")
    print("2. Add Product to Cart")
    print("3. Remove Product")
    print("4. Update Quantity")
    print("5. Display Cart")
    print("6. Calculate Total")
    print("7. Checkout")
    print("8. Exit")

    try:

        choice = int(
            input("Enter your choice: ")
        )

        # ------------------------------------------------
        # DISPLAY PRODUCTS
        # ------------------------------------------------

        if choice == 1:

            print("\n========== AVAILABLE PRODUCTS ==========")

            for product in products:

                product.display_product()

        # ------------------------------------------------
        # ADD PRODUCT
        # ------------------------------------------------

        elif choice == 2:

            try:

                product_id = int(input("Enter Product ID: "))

                product = find_product(products,product_id)
                quantity = int(input("Enter Quantity: "))

                cart.add_product(product,quantity)

            except ValueError:

                print("\nError: Please enter valid numeric data.")

            except ProductNotFoundException as e:

                print("\nError:", e)

            except InvalidQuantityException as e:

                print("\nError:", e)

            except InsufficientStockException as e:

                print("\nError:", e)

        # ------------------------------------------------
        # REMOVE PRODUCT
        # ------------------------------------------------

        elif choice == 3:

            try:

                product_id = int(input("Enter Product ID: "))

                cart.remove_product(product_id)

            except ValueError:

                print("\nError: Product ID must be numeric.")

            except ProductNotFoundException as e:

                print("\nError:", e)

        # ------------------------------------------------
        # UPDATE QUANTITY
        # ------------------------------------------------

        elif choice == 4:

            try:

                product_id = int(input("Enter Product ID: "))

                quantity = int(input("Enter New Quantity: "))

                cart.update_quantity(product_id,quantity)

            except ValueError:

                print("\nError: Please enter valid numeric data.")

            except ProductNotFoundException as e:

                print("\nError:", e)

            except InvalidQuantityException as e:

                print("\nError:", e)

            except InsufficientStockException as e:

                print("\nError:", e)

        # ------------------------------------------------
        # DISPLAY CART
        # ------------------------------------------------

        elif choice == 5:

            try:

                cart.display_cart()

            except EmptyCartException as e:

                print("\nError:", e)

        # ------------------------------------------------
        # CALCULATE TOTAL
        # ------------------------------------------------

        elif choice == 6:

            try:

                if len(cart.cart_items) == 0:

                    raise EmptyCartException("Cart is empty.")

                total = cart.calculate_total()

                print("\nTotal Cart Amount :: ₹", total)

            except EmptyCartException as e:

                print("\nError:", e)

        # ------------------------------------------------
        # CHECKOUT
        # ------------------------------------------------

        elif choice == 7:

            try:

                cart.checkout()

            except EmptyCartException as e:

                print("\nError:", e)

        # ------------------------------------------------
        # EXIT
        # ------------------------------------------------

        elif choice == 8:

            print("\nThank you for using Online Shopping System.")
            break

        else:

            print("\nError: Invalid menu choice.")

    except ValueError:

        print("\nError: Please enter a numeric menu choice.")
