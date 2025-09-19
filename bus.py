from ticket import Ticket
from person import Person

class Bus:

    def __init__(self, total_seats):
        self.__total_seats = total_seats
        self.__taken_seats = 0
        self.__tickets = []

    def get_total_seats(self):
        return self.__total_seats

    def set_total_seats(self, total_seats):
        self.__total_seats = total_seats

    def get_taken_seats(self):
        return self.__taken_seats

    def set_taken_seats(self, taken_seats):
        self.__taken_seats = taken_seats

    def sale_tickets(self, quantity):
        if self.get_taken_seats() + quantity > self.get_total_seats():
            print("No hay suficientes asientos disponibles para realizar la venta.")
            return
        
        name = input("Ingrese el nombre del pasajero: ")
        surname = input("Ingrese el apellido del pasajero: ")
        person = Person(name, surname)
        ticket = Ticket(quantity, "10/10/2023", person)
        self.__tickets.append(ticket)
        self.set_taken_seats(self.get_taken_seats() + quantity)
        print(f"Venta realizada. ID del ticket: {ticket.get_id()}")

    def refound_ticket(self, ticket_id):
        for ticket in self.__tickets:
            if ticket.get_id() == ticket_id:
                self.set_taken_seats(self.get_taken_seats() - ticket.get_seats())
                self.__tickets.remove(ticket)
                print(f"Ticket con ID {ticket_id} devuelto correctamente.")
                return
        print(f"No se encontró el ticket con ID {ticket_id}.")

    def sale_status(self):
        status = f"\nAsientos totales: {self.get_total_seats()}, Asientos ocupados: {self.get_taken_seats()}, Asientos disponibles: {self.get_total_seats() - self.get_taken_seats()}\n"
        if self.__tickets:
            status += "Tickets vendidos:\n"
            for ticket in self.__tickets:
                status += str(ticket)
        else:
            status += "No hay tickets vendidos."
        return status