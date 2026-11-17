from datetime import datetime

class Appointment:
    def __init__(self,appointment_id,patient_id,doctor,date):
        self.appointment_id=appointment_id
        self.patient_id=patient_id
        self.doctor=doctor
        self.date=date
        self.created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return self.__dict__


# #concepts
# DateTime Module
# automatic time Stamp
