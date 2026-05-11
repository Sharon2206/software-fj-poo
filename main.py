from modelos.cliente import cliente


try:

    cliente1 = cliente(
        1,
        "Sharon Angarita",
        "asdfg",
        "123456789"
    )

    print(cliente1.mostrar_informacion())

except Exception as e:
    print(f"error: {e}")