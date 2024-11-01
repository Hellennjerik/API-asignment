class Doctor:
    def __init__(self, name, age, gender, specialty, id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.specialty = specialty
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Specialty: {self.specialty}")
        print(f"ID Number: {self.id_number}")

class Patient:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID Number: {self.id_number}")

def main():
    doc1 = Doctor("Dr.Olive", 40, "Female", "Pediatrician", 101 )
    pat1 = Patient("Hellen", 10, 1)

    #displaying information using inheritance
    print("Doctor Information:")
    doc1.display_info() #calling the method from the parent class

    print("\nDisplaying Patient Information:")
    pat1.display_info() #calling the method from the parent class

if __name__ == "__main__":
    main()