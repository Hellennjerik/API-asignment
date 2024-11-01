# appointment.py

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def schedule(self):
        return f"Appointment scheduled for {self.patient.name} with Dr. {self.doctor.name} on {self.date_time}."

    def cancel(self):
        return f"Appointment with ID {self.appointment_id} has been canceled."




  