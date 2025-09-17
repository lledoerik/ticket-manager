class Bus:
    def __init__(self, total_seats):
        self.__total_seats = total_seats
        self.__taken_seats = total_seats

    def status_sale(self):
        return f"Asientos totales: {self.__asientos_totales}, Asientos ocupados: {self.__taken_seats}, Asientos disponibles: {self.__total_seats - self.__taken_seats}"
    
    def take_seats(self, number_of_tickets):
        if self.__taken_seats + number_of_tickets <= self.__total_seats:
            self.__taken_seats += number_of_tickets
            return f"Se han vendido {number_of_tickets} boletos."
        else:
            return "No hay suficientes asientos disponibles."
    
