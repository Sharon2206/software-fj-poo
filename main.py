from servicios.sala import sala
from servicios.equipo import equipo
from servicios.asesoria import asesoria


try:

    servicio1 = sala(
        1,
        "Sala premium",
        50000,
        20
    )

    servicio2 = equipo(
        2,
        "Portátil gamer",
        30000,
        "Computador"
    )

    servicio3 = asesoria(
        3,
        "Asesoria python",
        80000,
        "Ingeniero senior"
    )

    print(servicio1.describir_servicio())
    print("------------------")

    print(servicio2.describir_servicio())
    print("------------------")

    print(servicio3.describir_servicio())
    print("------------------")

    print("Costo sala:", servicio1.calcular_costo(3))
    print("Costo equipo:", servicio2.calcular_costo(2))
    print("Costo asesoria:", servicio3.calcular_costo(4, 10))

except Exception as e:
    print(f"Error: {e}")