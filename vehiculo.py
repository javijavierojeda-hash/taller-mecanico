class Vehiculo:
    """
    Clase que representa un vehículo dentro del sistema del Taller Mecánico.
    Todos sus atributos están encapsulados (son privados).
    """

    def __init__(self, patente: str, modelo: str, anio: int):
        # Al usar doble guion bajo (__), hacemos las variables privadas
        self.__patente = patente
        self.__modelo = modelo
        self.__anio = anio
        self.__en_taller = False

    # Getters y Setters (usando decoradores property) para acceder a las variables privadas de forma segura
    @property
    def patente(self):
        return self.__patente

    @patente.setter
    def patente(self, nueva_patente):
        self.__patente = nueva_patente

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, nuevo_anio):
        if nuevo_anio > 1885:  # Validación simple: el primer auto se inventó en 1886
            self.__anio = nuevo_anio
        else:
            print("Año inválido.")

    def ingresar(self):
        if not self.__en_taller:
            self.__en_taller = True
            print(f"El vehículo {self.__modelo} ({self.__patente}) ha ingresado al taller.")
        else:
            print(f"El vehículo {self.__modelo} ({self.__patente}) ya se encuentra en el taller.")

    def entregar(self):
        if self.__en_taller:
            self.__en_taller = False
            print(f"El vehículo {self.__modelo} ({self.__patente}) ha sido entregado al cliente.")
        else:
            print(f"El vehículo {self.__modelo} ({self.__patente}) no está actualmente en el taller.")

    def tarifa_hora(self) -> float:
        return 35.0  

    def __str__(self):
        estado = "En taller" if self.__en_taller else "Fuera del taller"
        return f"Vehículo [Patente: {self.__patente}, Modelo: {self.__modelo}, Año: {self.__anio}, Estado: {estado}]"

# Código de prueba rápido
if __name__ == "__main__":
    mi_auto = Vehiculo(patente="AB123CD", modelo="Toyota Corolla", anio=2021)
    
    # Probamos acceder a las variables de forma segura mediante los getters
    print(f"Auto ingresado: {mi_auto.modelo} del año {mi_auto.anio}")
    
    mi_auto.ingresar()
    mi_auto.entregar()
