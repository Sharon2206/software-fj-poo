from modelos.servicio import servicio
from excepciones.personalizadas import servicio_no_disponible_error
from utilidades.logger import registrar_log


class sala(servicio):

    def __init__(self, id_entidad, nombre, costo_base, capacidad):

        super().__init__(id_entidad, nombre, costo_base)

        if capacidad <= 0:
            registrar_log("Error: Capacidad invalida en sala")
            raise servicio_no_disponible_error(
                "La capacidad debe ser mayor a cero"
            )

        self.capacidad = capacidad

    def calcular_costo(self, horas=1):

        if horas <= 0:
            registrar_log("Error: Horas invalidas en sala")
            raise servicio_no_disponible_error(
                "Las horas deben ser mayores a cero"
            )

        return self._costo_base * horas

    def describir_servicio(self):

        return (
            f"Sala: {self._nombre}\n"
            f"Capacidad: {self.capacidad}\n"
            f"Costo por hora: {self._costo_base}"
        )

    def mostrar_informacion(self):
        return self.describir_servicio()