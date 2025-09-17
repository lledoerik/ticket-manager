class Bus:
    def __init__(self, total_seats):
        self.__total_seats = total_seats
        self.__taken_seats = 0

    def getTotalSeats(self):
        return self.__total_seats
    
    def setTotalSeats(self, total_seats):
        self.__total_seats = total_seats

    def getTakenSeats(self):
        return self.__taken_seats
    
    def setTakenSeats(self, taken_seats):
        self.__taken_seats = taken_seats

    def estado_venta(self):
        return f"Asientos totales: {self.getTotalSeats()}, Asientos ocupados: {self.getTakenSeats()}, Asientos disponibles: {self.getTotalSeats() - self.getTakenSeats()}"
    