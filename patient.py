
class Patient:

    def __init__(self, name: str, age: int, patient_id: str):

        self.name = name

        self.age = age

        self.patient_id = patient_id

        self.medical_history = []



    def add_medical_record(self, record: str) -> None:

        self.medical_history.append(record)



    def update_medical_record(self, old_record: str, new_record: str) -> None:

        if old_record in self.medical_history:

            self.medical_history[self.medical_history.index(old_record)] = new_record



    def delete_medical_record(self, record: str) -> None:

        if record in self.medical_history:

            self.medical_history.remove(record)



    def get_medical_history(self) -> list:

        return self.medical_history



    def get_info(self) -> str:

        return f"Patient Name: {self.name}, Age: {self.age}, ID: {self.patient_id}"

    
     