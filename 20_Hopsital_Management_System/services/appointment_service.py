from models.appointment import Appointment
from utils.file_handler import read_file, write_file
from utils.validators import validate_date

# APPOINTMENT_FILE = "data/appointments.json"

APPOINTMENT_FILE = "20_Hospital_Management_System/data/appointments.json"

def book_appointment():
    try:
        aid = input("Enter Appointment ID: ")
        pid = input("Enter Patient ID: ")
        doctor = input("Enter Doctor Name: ")
        date = input("Enter Date (YYYY-MM-DD): ")

        validate_date(date)

        appointments = read_file(APPOINTMENT_FILE)
        appointment = Appointment(aid, pid, doctor, date)
        appointments.append(appointment.to_dict())
        write_file(APPOINTMENT_FILE, appointments)

        print("Appointment Booked Successfully!")

    except ValueError as e:
        print("Error:", e)

def view_appointment():
    appointments = read_file(APPOINTMENT_FILE)

    print("\nID     PatientID   Doctor        Date        Created At")
    print("-"*70)

    for a in appointments:
        print(f"{a['appointment_id']:<6}{a['patient_id']:<12}{a['doctor']:<14}{a['date']:<12}{a['created_at']}")

