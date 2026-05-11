from modelos.servicio import servicio
from excepciones.personalizadas import servicio_no_disponible_error
from utilidades.logger import registrar_log


class equipo(servicio):

    def __init__(self, id_entidad, nombre, costo_base, tipo):

        super().__init__(id_entidad, nombre, costo_base)

        self.tipo = tipo

    def calcular_costo(self, dias=1):

        if dias <= 0:
            registrar_log("Error: Dias invalidos en equipo")
            raise servicio_no_disponible_error(
                "Los días deben ser mayores a cero"
            )

        return self._costo_base * dias

    def describir_servicio(self):

        return (
            f"Equipo: {self._nombre}\n"
            f"Tipo: {self.tipo}\n"
            f"Costo por día: {self._costo_base}"
        )

    def mostrar_informacion(self):
        return self.describir_servicio()