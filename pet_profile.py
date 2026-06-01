class Pet:
    def __init__(self):
        self.__name = "" ; self.__animal_type = "" ; self.__age = 0
    def get_name(self): return self.__name
    def get_animal_type(self): return self.__animal_type
    def get_age(self): return self.__age
    def set_name(self, name):
        if isinstance(name, str) and name.strip(): self.__name = name
    def set_animal_type(self, animal_type):
        if isinstance(animal_type, str) and animal_type.strip(): self.__animal_type = animal_type

    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.__age = age