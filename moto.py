# Importamos la clase base Vehiculo desde el archivo vehiculo.py
from vehiculo import Vehiculo

# Definimos la clase Moto que hereda de la clase base Vehiculo
class Moto(Vehiculo):

    # Sobrescribimos el método para devolver la tarifa por hora específica de Moto
    def tarifa_hora(self) -> int:
        # Retorna el valor fijo de 15000 como número entero (tarifa horaria para motos)
        return 15000
