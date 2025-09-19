class Ticket:
    _id_counter = 1
    
    def __init__(self, seats, date, person):
        self.__id = Ticket._id_counter
        Ticket._id_counter += 1
        self.__seats = seats
        self.__date = date
        self.__person = person

    def get_id(self):
        return self.__id

    def set_seats(self, seats):
        self.__seats = seats

    def get_seats (self):
        return self.__seats

    def set_date(self, date):
        self.__date = date

    def get_date (self):
        return self.__date

    def __str__(self):
        return f"Id Ticket: {self.__id}, seats: {self.__seats}, date: {self.__date}, person: {self.__person}"
