from abc import ABC, abstractmethod
from modelos.entidad import entidad


class servicio(entidad, ABC):

    def __init__(self, id_entidad, nombre, costo_base):
        super().__init__(id_entidad)

        self._nombre = nombre
        self._costo_base = costo_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_base(self):
        return self._costo_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass