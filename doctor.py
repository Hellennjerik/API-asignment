# doctor.py

from person import Person

class Doctor(Person):
    def __init__(self, name, age, gender, doctor_id, specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def diagnose(self, patient):
        return f"Doctor {self.name} diagnosed patient {patient.name}."
       
     
   