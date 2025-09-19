from bus import Bus

def mostrar_opciones_menu():
    print("\nSeleccione una opción:")
    print("1. Vender billetes")
    print("2. Devolver billetes")
    print("3. Mostrar estado de venta")
    print("0. Salir")

def menu(option):
    if option == "1":
        quantity = input("Ingrese la cantidad de billetes a comprar: ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Por favor, ingrese un número válido de billetes.")
        else:
            quantity = int(quantity)
            bus.sale_tickets(quantity)
    elif option == "2":
        ticket_id = input("Ingrese el ID del billete a devolver: ")
        if not ticket_id.isdigit() or int(ticket_id) <= 0:
            print("Por favor, ingrese un número válido de billetes.")
        else:
            bus.refound_ticket(int(ticket_id))
    elif option == "3":
        print(bus.sale_status())
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

total_seats = input("Ingrese el número de asientos del bus: ")
while total_seats.isdigit() == False or int(total_seats) <= 0:
    if not total_seats.isdigit() or int(total_seats) <= 0:
        print("Por favor, ingrese un número válido de asientos.")
        total_seats = input("Ingrese el número de asientos del bus: ")

bus = Bus(int(total_seats))

mostrar_opciones_menu()
option = input()

while option != "0":
    menu(option)
    mostrar_opciones_menu()
    option = input()
