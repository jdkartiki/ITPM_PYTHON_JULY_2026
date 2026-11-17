class Patient:
    def __init__(self,patient_id,name,age,gender):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.gender=gender

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"{self.patient_id:<10} {self.name:<50} {self.age:5} {self.gender:<10}"

# Concepts:
# Constructor
# Dunder MEthods -- dict, String
# interpolation