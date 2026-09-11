# -------------------------------
# Online Shopping Cart System
# -------------------------------

# Product List
products = [
    [101, "Laptop", 50000],
    [102, "Headphones", 2000],
    [103, "Mouse", 500],
    [104, "Keyboard", 1500]
]

# Cart List
cart = []


# -------------------------------
# Display Products
# -------------------------------
def view_products():
    print("\n" + "-"*40)
    print("        AVAILABLE PRODUCTS")
    print("-"*40)
    print("ID\tProduct Name\tPrice")
    print("-"*40)

    for p in products:
        print(f"{p[0]}\t{p[1]}\t\t₹{p[2]}")

    print("-"*40)


# -------------------------------
# Add Product to Cart
# -------------------------------
def add_to_cart():
    pid = int(input("Enter Product ID : "))
    qty = int(input("Enter Quantity : "))

    for p in products:
        if p[0] == pid:
            total_price = p[2] * qty
            cart.append([p[0], p[1], qty, total_price])
            print(f"\n✅ {p[1]} added to cart!")
            return

    print("❌ Product not found!")


# -------------------------------
# View Cart
# -------------------------------
def view_cart():
    if len(cart) == 0:
        print("\n⚠ Cart is Empty")
        return

    print("\n" + "-"*45)
    print("            YOUR CART")
    print("-"*45)
    print("Product Name\tQty\tPrice")
    print("-"*45)

    for item in cart:
        print(f"{item[1]}\t\t{item[2]}\t₹{item[3]}")

    print("-"*45)


# -------------------------------
# Remove Product
# -------------------------------
def remove_product():
    pid = int(input("Enter Product ID to remove : "))

    for item in cart:
        if item[0] == pid:
            cart.remove(item)
            print("✅ Product removed from cart")
            return

    print("❌ Product not found in cart")


# -------------------------------
# Generate Bill
# -------------------------------
def generate_bill():
    if len(cart) == 0:
        print("\n⚠ Cart is empty")
        return

    total = 0

    print("\n" + "-"*40)
    print("            BILL")
    print("-"*40)

    for item in cart:
        print(f"{item[1]}\t\t₹{item[3]}")
        total += item[3]

    print("-"*40)
    print(f"Total Amount = ₹{total}")
    print("-"*40)


# -------------------------------
# Menu Driven Program
# -------------------------------
while True:

    print("\n" + "="*40)
    print("      ONLINE SHOPPING CART")
    print("="*40)

    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Generate Bill")
    print("6. Exit")

    choice = int(input("\nEnter your choice : "))

    if choice == 1:
        view_products()

    elif choice == 2:
        add_to_cart()

    elif choice == 3:
        view_cart()

    elif choice == 4:
        remove_product()

    elif choice == 5:
        generate_bill()

    elif choice == 6:
        print("\nThank you for shopping with us 🛍️")
        break

    else:
        print("❌ Invalid Choice")