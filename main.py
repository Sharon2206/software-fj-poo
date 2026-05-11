from modelos.cliente import cliente
from modelos.reserva import reserva

from servicios.sala import sala
from servicios.equipo import equipo
from servicios.asesoria import asesoria

from utilidades.logger import registrar_log


# listas principales del sistema
clientes = []
servicios = []
reservas = []


# Carga servicios iniciales del sistema
try:

    sala1 = sala(
        1,
        "Sala premium",
        50000,
        20
    )

    equipo1 = equipo(
        2,
        "pc gamer",
        30000,
        "Computador"
    )

    asesoria1 = asesoria(
        3,
        "Asesoria python",
        80000,
        "Ingeniero senior"
    )

    servicios.append(sala1)
    servicios.append(equipo1)
    servicios.append(asesoria1)

except Exception as e:
    print(f"Error, cargando servicios: {e}")


# Muestra menú principal
def mostrar_menu():

    print("\n================================")
    print("         SOFTWARE FJ")
    print("================================")
    print("1. Registrar cliente")
    print("2. Mostrar servicios")
    print("3. Crear reserva")
    print("4. Procesar reservas")
    print("5. Mostrar clientes")
    print("6. Salir")
    print("================================")


# Registra nuevos clientes
def registrar_cliente():

    try:

        print("\n--- REGISTRO DE CLIENTE ---")

        id_cliente = len(clientes) + 1

        nombre = input("Nombre: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")

        nuevo_cliente = cliente(
            id_cliente,
            nombre,
            correo,
            telefono
        )

        clientes.append(nuevo_cliente)

        registrar_log(
            f"Cliente registrado: {nombre}"
        )

        print("\nCliente registrado correctamente")

    except Exception as e:

        registrar_log(
            f"Error registrando cliente: {e}"
        )

        print(f"\nError: {e}")


# Muestra servicios disponibles
def mostrar_servicios():

    print("\n--- SERVICIOS DISPONIBLES ---")

    for i, servicio in enumerate(servicios):

        print(f"\nServicio #{i + 1}")
        print(servicio.describir_servicio())


# Crea una nueva reserva
def crear_reserva():

    try:

        if len(clientes) == 0:

            print("\nNo hay clientes registrados")
            return

        print("\n--- CREAR RESERVA ---")

        print("\nClientes disponibles:")

        for i, c in enumerate(clientes):

            print(f"{i + 1}. {c.nombre}")

        cliente_index = int(
            input("\nSeleccione cliente: ")
        ) - 1

        cliente_seleccionado = clientes[cliente_index]

        print("\nServicios disponibles:")

        for i, s in enumerate(servicios):

            print(f"{i + 1}. {s.nombre}")

        servicio_index = int(
            input("\nSeleccione servicio: ")
        ) - 1

        servicio_seleccionado = servicios[servicio_index]

        duracion = int(
            input("Duración: ")
        )

        nueva_reserva = reserva(
            cliente_seleccionado,
            servicio_seleccionado,
            duracion
        )

        reservas.append(nueva_reserva)

        registrar_log(
            f"Reserva creada para: "
            f"{cliente_seleccionado.nombre}"
        )

        print("\nReserva creada correctamente")

    except Exception as e:

        registrar_log(
            f"Error creando reserva: {e}"
        )

        print(f"\nError: {e}")


def procesar_reservas():

    try:

        # Valida si existen reservas
        
        if len(reservas) == 0:

            print("\nNo hay reservas")
            return

        print("\n--- RESERVAS ---")

        for i, r in enumerate(reservas):

            print(f"\nReserva #{i + 1}")
            print(r.mostrar_reserva())

        opcion = int(
            input("\nEeleccione reserva: ")
        ) - 1

        reserva_seleccionada = reservas[opcion]

        costo = reserva_seleccionada.procesar_reserva()

        reserva_seleccionada.confirmar_reserva()

        print(f"\nCosto total: {costo}")

        print("\nReserva confirmada")

    except Exception as e:

        registrar_log(
            f"Error procesando reserva: {e}"
        )

        print(f"\nError: {e}")


def mostrar_clientes():

    # Valida si existen clientes

    if len(clientes) == 0:

        print("\nNo hay clientes registrados")
        return

    print("\n--- CLIENTES ---")

    for c in clientes:

        print("\n----------------")
        print(c.mostrar_informacion())


while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        registrar_cliente()

    elif opcion == "2":

        mostrar_servicios()

    elif opcion == "3":

        crear_reserva()

    elif opcion == "4":

        procesar_reservas()

    elif opcion == "5":

        mostrar_clientes()

    elif opcion == "6":

        print("\nSaliendo del sistema...")
        break

    else:

        print("\nOpción inválida")