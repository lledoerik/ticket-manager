class Bus:
    def __init__(self, total_seats):
        self.__total_seats = total_seats
        self.__taken_seats = total_seats

    def estado_venta(self):
        return f"Asientos totales: {self.__total_seats}, Asientos ocupados: {self.__taken_seats}, Asientos disponibles: {self.__total_seats - self.__taken_seats}"