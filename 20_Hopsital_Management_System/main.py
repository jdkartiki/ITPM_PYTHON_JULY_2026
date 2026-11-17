from services.patient_service import add_patient, view_patients
from services.appointment_service import book_appointment, view_appointment

def menu():
    while True:
        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Book Appointment")
        print("4. View Appointments")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            book_appointment()
        elif choice == "4":
            view_appointment()
        elif choice == "5":
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    menu()
