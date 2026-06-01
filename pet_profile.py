class Pet:
    def __init__(self):
        self.__name = ""; self.__animal_type = ""; self.__age = 0

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if isinstance(name, str) and name.strip(): self.__name = name

    def set_animal_type(self, animal_type):
        if isinstance(animal_type, str) and animal_type.strip(): self.__animal_type = animal_type

    def set_age(self, age):
        if isinstance(age, int) and age >= 0: self.__age = age


def execute_pet_registration_system():
    print("=== VETERINARY CLINIC REGISTRATION INTERFACE ===")
    registered_pet = Pet()

    input_name = input("Enter the official name of the pet: ").strip()
    input_type = input("Enter the classification species (e.g., Dog, Cat, Bird): ").strip()

    while True:
        try:
            input_age = int(input("Enter the chronological age of the animal: "))
            if input_age >= 0: break
            print("Age tracking matrices must reflect non-negative numbers.")
        except ValueError:
            print("Invalid value. Please specify a correct integer representation.")

    registered_pet.set_name(input_name)
    registered_pet.set_animal_type(input_type)
    registered_pet.set_age(input_age)

    print("\n--- VERIFIED REGISTRATION METRICS ---")
    print(f"Registered Alias      : {registered_pet.get_name()}")
    print(f"Biological Family Type: {registered_pet.get_animal_type()}")
    print(f"Documented Lifespan   : {registered_pet.get_age()} years old")


if __name__ == "__main__":
    execute_pet_registration_system()