class Vehiculo:
    """
    Clase que representa un vehículo dentro del sistema del Taller Mecánico.
    """

    def __init__(self, patente: str, modelo: str, anio: int):
        self.patente = patente
        self.modelo = modelo
        self.anio = anio
        self.__en_taller = False  # Único atributo privado

    def ingresar(self):
        if not self.__en_taller:
            self.__en_taller = True
            print(f"El vehículo {self.modelo} ({self.patente}) ha ingresado al taller.")
        else:
            print(f"El vehículo {self.modelo} ({self.patente}) ya se encuentra en el taller.")

    def entregar(self):
        if self.__en_taller:
            self.__en_taller = False
            print(f"El vehículo {self.modelo} ({self.patente}) ha sido entregado al cliente.")
        else:
            print(f"El vehículo {self.modelo} ({self.patente}) no está actualmente en el taller.")

    def tarifa_hora(self) -> float:
        return 35.0  

    def __str__(self):
        estado = "En taller" if self.__en_taller else "Fuera del taller"
        return f"Vehículo [Patente: {self.patente}, Modelo: {self.modelo}, Año: {self.anio}, Estado: {estado}]"

# Código de prueba rápido
if __name__ == "__main__":
    mi_auto = Vehiculo(patente="AB123CD", modelo="Toyota Corolla", anio=2021)
    print(mi_auto)
    
    mi_auto.ingresar()
    mi_auto.entregar()
