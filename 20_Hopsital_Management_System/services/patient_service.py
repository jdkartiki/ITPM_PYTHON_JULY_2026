from models.patient import Patient
from utils.file_handler import read_file,write_file
from utils.validators import validate_age

PATIENT_FILE="data/patients.json"

def add_patient():
    try:
        pid=input("Enter Patient ID :: ")
        name=input("Enter Name :: ")
        age=int(input("Enter Age :: "))
        gender=input("Enter Gender :: ")

        validate_age(age)

        patients=read_file(PATIENT_FILE)
        patient=Patient(pid,name,age,gender)
        patients.append(patient.to_dict())
        write_file(PATIENT_FILE,patients)

        print("Patient Added Successfully")
    except ValueError as e:
        print("Error :: ",e)


def view_patients():
    patients=read_file(PATIENT_FILE)

    print("\nID              NAME             AGE        GENDER")
    print("-"*50)

    for p in patients:
        print(f"{p['patient_id']:<10} {p['name']:<20} {p['age']:<5} {p['gender']:<10}")