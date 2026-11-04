from inventory_manager import InventoryManager

def menu():
    print("\n====== INVENTORY SYSTEM ======")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Generate Bill")
    print("5. Exit")

def main():
    manager = InventoryManager()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_product()

        elif choice == "2":
            manager.view_products()

        elif choice == "3":
            manager.update_stock()

        elif choice == "4":
            manager.billing()

        elif choice == "5":
            print("Exiting... 👋")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()