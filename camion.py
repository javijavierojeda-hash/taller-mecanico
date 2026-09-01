# Importamos la clase base Vehiculo desde el archivo vehiculo.py
from vehiculo import Vehiculo

# Definimos la clase Camion que hereda de la clase base Vehiculo
class Camion(Vehiculo):

    # Definimos el constructor que recibe patente, anio, capacidad_carga y modelo opcional
    def __init__(self, patente: str, anio: int, capacidad_carga: int, modelo: str = "Camión"):
        # Llamamos al constructor de la clase padre (Vehiculo) para inicializar los atributos heredados
        super().__init__(patente, modelo, anio)
        # Guardamos la capacidad de carga (en kilos) como un atributo privado con __
        self.__capacidad_carga = capacidad_carga
