from person import Person  # Import Person class from person module

class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age) 
        self.patient_id = patient_id # Unique identifier for the patients
        self.medical_history = []

    def display_info(self):
        print("Patient Information:")   
        super().display_info()
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.patient_id}")

    def add_medical_history(self, record):
        self.medical_history.append(record)

    def update_medical_record(self, old_record, new_record):
        #update a record in the medical history
        if old_record in self.medical_history:
            index = self.medical_history.index(old_record)
            self.medical_history[index] = new_record
        else:
            print("Record not found")

    def delete_medical_record(self, record):
        #delete a record from the medical history
        if record in self.medical_history:
            self.medical_history.remove(record)
        else:
            print("Record not found")   
            
    def get_medical_history(self):
        return self.medical_history
    
     