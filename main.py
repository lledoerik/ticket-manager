from bus import Bus


def menu(option):
    if option == 1:
        bus.venta_billetes()
    elif option == 2:
        bus.devolucion_billetes()
    elif option == 3:
        print(bus.sale_status())


total_seats = int(input("Ingrese el número de asientos del bus: "))
bus = Bus(total_seats)

print("1.- Venta de billetes.")
print("2.- Devolución de billetes.")
print("3.- Estado de la venta.")
print("0.- Salir.")
option = int(input())

while option != 0:
    menu(option)
    option = int(input())
