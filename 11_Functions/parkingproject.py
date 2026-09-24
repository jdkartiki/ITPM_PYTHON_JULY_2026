import time

def park_vehicle(parking):
    vehicle_no = input("Enter vehicle number: ")
    vehicle_type = input("Enter type (2W/4W): ")

    if vehicle_no in parking:
        print("❌ Vehicle already parked!")
        return

    entry_time = time.time()

    parking[vehicle_no] = {
        "type": vehicle_type,
        "entry_time": entry_time
    }

    print("✅ Vehicle parked successfully!")


def remove_vehicle(parking):
    vehicle_no = input("Enter vehicle number to exit: ")

    if vehicle_no not in parking:
        print("❌ Vehicle not found!")
        return

    exit_time = time.time()
    entry_time = parking[vehicle_no]["entry_time"]

    duration = (exit_time - entry_time) / 60  # in minutes

    charge = calculate_charge(duration, parking[vehicle_no]["type"])

    print(f"\n🚗 Vehicle: {vehicle_no}")
    print(f"⏱️ Time parked: {round(duration, 2)} minutes")
    print(f"💰 Parking Charge: ₹{charge}")

    del parking[vehicle_no]
    print("✅ Vehicle exited!")


def calculate_charge(duration, vehicle_type):
    if vehicle_type == "2W":
        return max(10, int(duration) * 2)
    else:
        return max(20, int(duration) * 5)


def view_parking(parking):
    if not parking:
        print("Parking is empty.")
        return

    print("\n📋 Parked Vehicles:")
    for v_no, details in parking.items():
        print(f"{v_no} | Type: {details['type']}")


def parking_status(parking, capacity):
    occupied = len(parking)
    available = capacity - occupied

    print(f"\n🅿️ Total Slots: {capacity}")
    print(f"🚗 Occupied: {occupied}")
    print(f"🟢 Available: {available}")


def main():
    parking = {}
    capacity = int(input("Enter total parking capacity: "))

    while True:
        print("\n===== SMART PARKING SYSTEM =====")
        print("1. Park Vehicle")
        print("2. Remove Vehicle")
        print("3. View Parked Vehicles")
        print("4. Parking Status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if len(parking) >= capacity:
                print("❌ Parking Full!")
            else:
                park_vehicle(parking)

        elif choice == "2":
            remove_vehicle(parking)

        elif choice == "3":
            view_parking(parking)

        elif choice == "4":
            parking_status(parking, capacity)

        elif choice == "5":
            print("👋 Exiting system...")
            break

        else:
            print("❌ Invalid choice!")


# Run program
main()
