# Importamos la clase base Vehiculo desde el archivo vehiculo.py
from vehiculo import Vehiculo

# Definimos la clase Auto que hereda de la clase base Vehiculo
class Auto(Vehiculo):

    # Definimos el constructor que recibe los datos del vehiculo y la capacidad del maletero (litros)
    def __init__(self, patente: str, modelo: str, anio: int, capacidad_maletero: int = 400):
        # Llamamos al constructor de la clase padre para inicializar los atributos comunes
        super().__init__(patente, modelo, anio)
        # Guardamos la capacidad del maletero como un atributo privado con __
        self.__capacidad_maletero = capacidad_maletero
