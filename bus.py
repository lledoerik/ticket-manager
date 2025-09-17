class Bus:

    def __init__(self, total_seats):
        self.__total_seats = total_seats
        self.__taken_seats = 0

    def get_total_seats(self):
        return self.__total_seats

    def set_total_seats(self, total_seats):
        self.__total_seats = total_seats

    def get_taken_seats(self):
        return self.__taken_seats

    def set_taken_seats(self, taken_seats):
        self.__taken_seats = taken_seats

    def sale_tickets(self):
        pass

    def refound_ticket(self):
        pass

    def sale_status(self):
        return f"Asientos totales: {self.get_total_seats()}, Asientos ocupados: {self.get_taken_seats()}, Asientos disponibles: {self.get_total_seats() - self.get_taken_seats()}"
