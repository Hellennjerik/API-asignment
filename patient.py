from person import Person  # Import Person class from person module

class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age) # Inheriting from the Person class
        self.patient_id = patient_id # Unique identifier for the patients
        self.medical_history = []

    def display_info(self):
        super().display_info()
        print(f"Patient ID: {self.patient_id}")

    def add_medical_history(self, record):
        self.medical_history.append(record)

    def get_medical_history(self):
        return self.medical_history
    
     