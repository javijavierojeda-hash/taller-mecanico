from model.vehiculo import Vehiculo
from model.modelo import Modelo

class Moto(Vehiculo):
    def __init__(self, patente: str, anio: int, modelo: Modelo):
        super().__init__(patente, anio, modelo)
        
    def tarifa_hora(self) -> int:
        return 15000
