from file_handler import load_data, save_data

class InventoryManager:

    def __init__(self):
        self.products = load_data()

    def add_product(self):
        try:
            pid = input("Enter Product ID: ")

            for p in self.products:
                if p["id"] == pid:
                    print("Product ID already exists!")
                    return

            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))

            self.products.append({
                "id": pid,
                "name": name,
                "price": price,
                "qty": qty
            })

            save_data(self.products)
            print("Product added!")

        except:
            print("Invalid input!")

    def view_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\nProduct List:")
        for p in self.products:
            print(f"{p['id']} | {p['name']} | Rs. {p['price']} | Stock: {p['qty']}")

    def update_stock(self):
        pid = input("Enter Product ID: ")

        for p in self.products:
            if p["id"] == pid:
                try:
                    print("\n1. Add Stock")
                    print("2. Set Stock")

                    choice = input("Enter choice: ")
                    qty = int(input("Enter quantity: "))

                    if qty < 0:
                        print("Quantity cannot be negative!")
                        return

                    if choice == "1":
                        p["qty"] += qty   
                    elif choice == "2":
                        p["qty"] = qty    
                    else:
                        print("Invalid choice!")
                        return

                    save_data(self.products)
                    print(f"Stock updated! New quantity: {p['qty']}")
                    return

                except:
                    print("Invalid input!")
                    return

        print("Product not found!")

    def billing(self):
        cart = []
        total = 0

        while True:
            pid = input("Enter Product ID (or 'done'): ")

            if pid.lower() == "done":
                break

            product = next((p for p in self.products if p["id"] == pid), None)

            if not product:
                print("Product not found!")
                continue

            try:
                qty = int(input("Enter quantity: "))

                if qty > product["qty"]:
                    print("Not enough stock!")
                    continue

                cost = qty * product["price"]
                total += cost

                product["qty"] -= qty

                cart.append({
                    "name": product["name"],
                    "qty": qty,
                    "cost": cost
                })

            except:
                print("Invalid input!")

        # Save updated stock
        save_data(self.products)

        # Bill print
        print("\nBILL")
        for item in cart:
            print(f"{item['name']} x {item['qty']} = ₹{item['cost']}")

        gst = total * 0.18
        final = total + gst

        print(f"\nSubtotal: Rs. {total}")
        print(f"GST (18%): Rs. {gst}")
        print(f"Total Amount: Rs. {final}")