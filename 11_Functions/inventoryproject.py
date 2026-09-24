def add_product(inventory):
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    qty = int(input("Enter Quantity: "))

    inventory[pid] = {
        "name": name,
        "price": price,
        "qty": qty
    }

    print("✅ Product added successfully!")


def view_inventory(inventory):
    if not inventory:
        print("Inventory empty!")
        return

    print("\n📦 Inventory:")
    for pid, details in inventory.items():
        print(f"{pid} | {details['name']} | ₹{details['price']} | Qty: {details['qty']}")


def update_stock(inventory):
    pid = input("Enter Product ID: ")

    if pid in inventory:
        qty = int(input("Enter quantity to add: "))
        inventory[pid]["qty"] += qty
        print("✅ Stock updated!")
    else:
        print("❌ Product not found!")


def low_stock_alert(inventory):
    print("\n⚠️ Low Stock Products (Qty < 5):")
    found = False

    for pid, details in inventory.items():
        if details["qty"] < 5:
            print(f"{details['name']} (Qty: {details['qty']})")
            found = True

    if not found:
        print("All products have sufficient stock.")


def create_bill(inventory):
    bill = []
    total = 0

    while True:
        pid = input("Enter Product ID (or 'done'): ")

        if pid == "done":
            break

        if pid not in inventory:
            print("❌ Product not found!")
            continue

        qty = int(input("Enter quantity: "))

        if qty > inventory[pid]["qty"]:
            print("❌ Not enough stock!")
            continue

        price = inventory[pid]["price"]
        cost = price * qty

        inventory[pid]["qty"] -= qty

        bill.append({
            "name": inventory[pid]["name"],
            "qty": qty,
            "cost": cost
        })

        total += cost
        print("✅ Item added to bill")

    print_bill(bill, total)


def print_bill(bill, total):
    print("\n🧾 ===== INVOICE =====")

    for item in bill:
        print(f"{item['name']} x {item['qty']} = ₹{item['cost']}")

    tax = total * 0.05
    grand_total = total + tax

    print(f"\nSubtotal: ₹{total}")
    print(f"GST (5%): ₹{round(tax,2)}")
    print(f"💰 Total Payable: ₹{round(grand_total,2)}")
    print("======================")


def main():
    inventory = {}

    while True:
        print("\n===== INVENTORY & BILLING SYSTEM =====")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Stock")
        print("4. Low Stock Alert")
        print("5. Create Bill")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product(inventory)

        elif choice == "2":
            view_inventory(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            low_stock_alert(inventory)

        elif choice == "5":
            create_bill(inventory)

        elif choice == "6":
            print("👋 Exiting system...")
            break

        else:
            print("❌ Invalid choice!")


# Run
main()
