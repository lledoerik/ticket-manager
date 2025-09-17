class Person:
    dni = None

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_surname(self, surname):
        self.__surname = surname

    def get_surname(self):
        return self.__surname

    def __str__(self):
        return f"Name: {self.__name}\nSurname: {self.__surname}"