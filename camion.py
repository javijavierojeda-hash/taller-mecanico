from vehiculo import Vehiculo
from modelo import Modelo

class Camion(Vehiculo):
    def __init__(self, patente: str, anio: int, modelo: Modelo, capacidad_carga: int):
        super().__init__(patente, anio, modelo)
        self.__capacidad_carga: int = capacidad_carga

    def tarifa_hora(self) -> int:
        return 40000
