from modelos.cliente import cliente
from modelos.reserva import reserva

from servicios.sala import sala
from servicios.equipo import equipo
from servicios.asesoria import asesoria

from utilidades.logger import registrar_log


print("===================================")
print("      Sistema software fj")
print("===================================")


clientes = []
servicios = []
reservas = []


# operacion 1
try:

    cliente1 = cliente(
        1,
        "Sharon Angarita",
        "sharon@gmail.com",
        "123456789"
    )

    clientes.append(cliente1)

    print("\nCliente registrado correctamente")

except Exception as e:

    print(f"\nError: {e}")


# operacion 2
try:

    cliente2 = cliente(
        2,
        "ab",
        "correo_malo",
        "Teléfono"
    )

    clientes.append(cliente2)

except Exception as e:

    print(f"\nError cliente inválido: {e}")


# operacion 3
try:

    sala1 = sala(
        1,
        "Sala premium",
        50000,
        20
    )

    servicios.append(sala1)

    print("\nSala creada correctamente")

except Exception as e:

    print(f"\nError creando sala: {e}")


# operacion 4
try:

    sala_invalida = sala(
        2,
        "Sala pequeña",
        30000,
        -5
    )

    servicios.append(sala_invalida)

except Exception as e:

    print(f"\nError sala invalida: {e}")


# operacion 5
try:

    equipo1 = equipo(
        3,
        "pc gamer",
        40000,
        "Computador"
    )

    servicios.append(equipo1)

    print("\nEquipo registrado correctamente")

except Exception as e:

    print(f"\nError equipo: {e}")


# operacion 6
try:

    asesoria1 = asesoria(
        4,
        "Asesoria python",
        80000,
        "Ingeniero senior"
    )

    servicios.append(asesoria1)

    print("\nAsesoria creada correctamente")

except Exception as e:

    print(f"\nError asesoria: {e}")


# operacion 7
try:

    reserva1 = reserva(
        clientes[0],
        sala1,
        3
    )

    reservas.append(reserva1)

    print("\nReserva creada correctamente")

except Exception as e:

    print(f"\nError reserva: {e}")


# operacion 8
try:

    reserva_invalida = reserva(
        clientes[0],
        equipo1,
        -2
    )

    reservas.append(reserva_invalida)

except Exception as e:

    print(f"\nError reserva invalida: {e}")


# operacion 9
try:

    costo = reserva1.procesar_reserva()

    print(f"\nCosto reserva: {costo}")

    reserva1.confirmar_reserva()

    print("\nReserva confirmada")

except Exception as e:

    print(f"\nError, procesando reserva: {e}")


# operacion 10
try:

    reserva1.cancelar_reserva()

except Exception as e:

    print(f"\nError, cancelando reserva: {e}")


print("\n===================================")
print(" Sistema ejecutado correctamente")
print("===================================")