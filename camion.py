# Importamos la clase base Vehiculo desde el archivo vehiculo.py
from vehiculo import Vehiculo

# Definimos la clase Camion que hereda de la clase base Vehiculo
class Camion(Vehiculo):

    # Definimos el constructor que recibe patente, anio, capacidad_carga y modelo opcional
    def __init__(self, patente: str, anio: int, capacidad_carga: int, modelo: str = "Camión"):
        # Llamamos al constructor de la clase padre (Vehiculo) para inicializar los atributos heredados
        super().__init__(patente, modelo, anio)
        # Asignamos la capacidad de carga a través del setter para validarla
        self.capacidad_carga = capacidad_carga

    # --- PROPIEDAD: CAPACIDAD CARGA ---
    # Definimos el getter para acceder a la capacidad privada de carga
    @property
    def capacidad_carga(self) -> int:
        return self.__capacidad_carga

    # Definimos el setter para validar que la capacidad de carga sea válida
    @capacidad_carga.setter
    def capacidad_carga(self, valor: int):
        try:
            valor_int = int(valor)
        except (ValueError, TypeError):
            print(f"  [ERROR DE VALIDACION] La capacidad de carga '{valor}' debe ser un numero entero (en kg).")
            raise ValueError(f"Capacidad de carga invalida: '{valor}'. Debe ser un numero entero.")

        if valor_int <= 0 or valor_int > 100000:
            print(f"  [ERROR DE VALIDACION] La capacidad de carga ({valor_int} kg) debe estar entre 1 y 100000 kg.")
            raise ValueError(f"Capacidad de carga fuera de rango: {valor_int} kg.")

        self.__capacidad_carga = valor_int
        print(f"  [VALIDACION EXITOSA] Capacidad de carga de {valor_int} kg asignada correctamente.")

    # Sobrescribimos el método para devolver la tarifa por hora específica de Camion
    def tarifa_hora(self) -> int:
        # Retorna el valor fijo de 40000 como número entero
        return 40000
