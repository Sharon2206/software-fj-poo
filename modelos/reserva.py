from excepciones.personalizadas import (
    reserva_invalida_error,
    duracion_invalida_error
)

from utilidades.logger import registrar_log


class reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            registrar_log("Error: Duración inválida en reserva")
            raise duracion_invalida_error(
                "La duración debe ser mayor a cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar_reserva(self):

        try:

            if self.estado == "Cancelada":
                raise reserva_invalida_error(
                    "No se puede confirmar una reserva cancelada"
                )

            self.estado = "Confirmada"

            registrar_log(
                f"Reserva confirmada para: {self.cliente.nombre}"
            )

        except Exception as e:

            registrar_log(f"Error al confirmar reserva: {e}")
            raise

    def cancelar_reserva(self):

        try:

            if self.estado == "Confirmada":
                raise reserva_invalida_error(
                    "No se puede cancelar una reserva confirmada"
                )

            self.estado = "Cancelada"

            registrar_log(
                f"Reserva cancelada para {self.cliente.nombre}"
            )

        except Exception as e:

            registrar_log(f"Error al cancelar reserva: {e}")
            raise

    def procesar_reserva(self):

        try:

            costo = self.servicio.calcular_costo(self.duracion)

        except Exception as e:

            registrar_log(
                f"Error procesando reserva: {e}"
            )

            raise reserva_invalida_error(
                "Fallo el procesamiento de la reserva"
            ) from e

        else:

            registrar_log(
                f"Reserva realizada correctamente para: "
                f"{self.cliente.nombre}"
            )

            return costo

        finally:

            registrar_log(
                "Finalizó el proceso de reserva"
            )

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}"
        )