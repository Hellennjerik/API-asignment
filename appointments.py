class Appointment:
    def __init__(self, appointment_id, description, doctor, patient, date, time):  
        self.appointment_id = appointment_id
        self.description = description
        self.doctor = doctor  # Reference to a Doctor object
        self.patient = patient  # Reference to a Patient object
        self.date = date
        self.time = time

    def display(self):
        print("Appointment Information:")
        print(f"Appointment ID: {self.appointment_id}, Description: {self.description}, Doctor: {self.doctor.name}, Patient: {self.patient.name}, Date: {self.date}, Time: {self.time}")  








  