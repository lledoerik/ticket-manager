class Ticket:

    def __init__(self, seat, date, person):
        self.__seat = seat
        self.__date = date
        self.__person = person

    def set_seat(self, seat):
        self.__seat = seat

    def get_seat (self):
        return self.__seat

    def set_date(self, date):
        self.__date = date

    def get_date (self, date):
        return self.__date

    def __str__(self):
        return f"Seat: {self.__seat}\nDate: {self.__date}\nPerson: {self.__person}"
