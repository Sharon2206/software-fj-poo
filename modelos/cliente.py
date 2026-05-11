from modelos.entidad import entidad
from excepciones.personalizadas import cliente_invalido_error
from utilidades.logger import registrar_log


# Clase que maneja la información de los clientes

class cliente(entidad):

    def __init__(self, id_entidad, nombre, correo, telefono):
        super().__init__(id_entidad)

        self.__nombre = None
        self.__correo = None
        self.__telefono = None

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        # Valida longitud mínima

        if not valor or len(valor.strip()) < 3:
            registrar_log("Error: Nombre de cliente inválido")
            raise cliente_invalido_error(
                "El nombre debe tener mínimo 3 caracteres"
            )

        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        # Valida formato del correo

        if "@" not in valor or "." not in valor:
            registrar_log("Error: Correo inválido")
            raise cliente_invalido_error(
                "Correo invalido"
            )

        self.__correo = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        # Valida que el teléfono solo tenga números

        if not valor.isdigit():
            registrar_log("Error: Teléfono inválido")
            raise cliente_invalido_error(
                "El teléfono solo debe contener números"
            )

        self.__telefono = valor

    def mostrar_informacion(self):

        return (
            f"id: {self.id_entidad}\n"
            f"nombre: {self.__nombre}\n"
            f"correo: {self.__correo}\n"
            f"telefono: {self.__telefono}"
        )