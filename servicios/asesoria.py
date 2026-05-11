from modelos.servicio import servicio
from excepciones.personalizadas import servicio_no_disponible_error
from utilidades.logger import registrar_log


class asesoria(servicio):

    def __init__(self, id_entidad, nombre, costo_base, especialista):

        super().__init__(id_entidad, nombre, costo_base)

        self.especialista = especialista

    def calcular_costo(self, horas=1, descuento=0):

        if horas <= 0:
            registrar_log("Error: Horas invalidas en asesoria")
            raise servicio_no_disponible_error(
                "Las horas deben ser mayores a cero"
            )

        total = self._costo_base * horas

        # Aplica descuento (si existe)

        if descuento > 0:
            total -= total * (descuento / 100)

        return total

    def describir_servicio(self):

        return (
            f"Asesoria: {self._nombre}\n"
            f"Especialista: {self.especialista}\n"
            f"Costo por hora: {self._costo_base}"
        )

    def mostrar_informacion(self):
        return self.describir_servicio()