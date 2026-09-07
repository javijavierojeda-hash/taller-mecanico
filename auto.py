# Importamos la clase base Vehiculo desde el archivo vehiculo.py
from vehiculo import Vehiculo

# Definimos la clase Auto que hereda de la clase base Vehiculo
class Auto(Vehiculo):

    # Definimos el constructor que recibe los datos del vehiculo y la capacidad del maletero (litros)
    def __init__(self, patente: str, modelo: str, anio: int, capacidad_maletero: int = 400):
        # Llamamos al constructor de la clase padre para inicializar los atributos comunes
        super().__init__(patente, modelo, anio)
        # Asignamos la capacidad del maletero a través del setter para validarla
        self.capacidad_maletero = capacidad_maletero

    # --- PROPIEDAD: CAPACIDAD MALETERO ---
    # Definimos el getter para acceder a la capacidad privada del maletero
    @property
    def capacidad_maletero(self) -> int:
        return self.__capacidad_maletero

    # Definimos el setter para validar que la capacidad sea un número positivo razonable
    @capacidad_maletero.setter
    def capacidad_maletero(self, valor: int):
        try:
            valor_int = int(valor)
        except (ValueError, TypeError):
            print(f"  [ERROR DE VALIDACION] La capacidad '{valor}' debe ser un numero entero (en litros).")
            raise ValueError(f"Capacidad invalida: '{valor}'. Debe ser un numero entero.")

        if valor_int <= 0 or valor_int > 3000:
            print(f"  [ERROR DE VALIDACION] La capacidad del maletero ({valor_int} L) debe estar entre 1 y 3000 litros.")
            raise ValueError(f"Capacidad {valor_int} L fuera de rango. Debe ser entre 1 y 3000 litros.")

        self.__capacidad_maletero = valor_int
        print(f"  [VALIDACION EXITOSA] Capacidad de maletero de {valor_int} L asignada correctamente.")

    # Sobrescribimos el método para devolver la tarifa por hora específica de Auto
    def tarifa_hora(self) -> int:
        # Retorna el valor fijo de 25000 como número entero
        return 25000
