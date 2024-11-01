
from datetime import datetime
from patient import Patient
from doctor import Doctor
from appointments import Appointment

if __name__ == "__main__":
    # Create instances of Patient and Doctor
    p1 = Patient("Julian", 10, "1")
    d1 = Doctor("Dr. Olive", 45, "Female", "101", "Pediatrician")

    # Add medical records for the patient
    p1.add_medical_record("Allergy to red meat")
    print("Medical History after adding:", p1.get_medical_history())

    # Update a medical record
    p1.update_medical_record("Allergy to red meat", "Severe allergy to red meat")
    print("Medical History after updating:", p1.get_medical_history())

    # Delete a medical record
    p1.delete_medical_record("Severe allergy to red meat")
    print("Medical History after deleting:", p1.get_medical_history())

    # Schedule an appointment
    app1 = Appointment("A001", p1, d1, datetime.now())
    
    # Print information
    print(p1.get_info())
    print(d1.diagnose(p1))
    print(app1.schedule())