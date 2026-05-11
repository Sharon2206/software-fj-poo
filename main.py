from modelos.cliente import cliente
from modelos.reserva import reserva

from servicios.sala import sala
from servicios.equipo import equipo
from servicios.asesoria import asesoria


print("sistema software fj")
print("---------------------------")


try:

    cliente1 = cliente(
        1,
        "sharon angarita",
        "sharon@gmail.com",
        "3201234567"
    )

    sala1 = sala(
        1,
        "sala premium",
        50000,
        15
    )

    equipo1 = equipo(
        2,
        "pc gamer",
        30000,
        "computador"
    )

    asesoria1 = asesoria(
        3,
        "asesoria python",
        80000,
        "ingeniero senior"
    )

    reserva1 = reserva(
        cliente1,
        sala1,
        -5
    )

    print(reserva1.mostrar_reserva())

    costo = reserva1.procesar_reserva()

    print("---------------------------")
    print(f"costo total: {costo}")

    reserva1.confirmar_reserva()

    print("---------------------------")
    print("reserva confirmada")
    print(reserva1.mostrar_reserva())

except Exception as e:

    print(f"error del sistema: {e}")