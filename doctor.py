from person import Person  # Import Person class from person module

class Doctor(Person):
    def __init__(self, name, age, gender, specialization, doctor_id):
        super().__init__(name, age) # call the instructor of Person

        # Attributes specific to the Doctor class
        self.gender = gender
        self.specialization = specialization
        self.doctor_id = doctor_id  # Unique identifier for the doctors

        def display_info(self):
            super().display_info()
            print(f"Gender: {self.gender}, Specialization: {self.specialization}, ID: {self.doctor_id}")

   