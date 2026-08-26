class Vehiculo:
    """
    Clase que representa un vehículo dentro del sistema del Taller Mecánico.
    """

    def __init__(self, patente: str, modelo: str, anio: int):
        """
        Constructor de la clase Vehiculo.
        
        Parámetros:
        - patente (str): La matrícula o placa del vehículo.
        - modelo (str): El modelo del vehículo.
        - anio (int): El año de fabricación del vehículo.
        """
        self.patente = patente
        self.modelo = modelo
        self.anio = anio
        self.__en_taller = False  # Atributo privado (encapsulado)

    def ingresar(self):
        """Marca el vehículo como ingresado al taller."""
        if not self.__en_taller:
            self.__en_taller = True
            print(f"El vehículo {self.modelo} ({self.patente}) ha ingresado al taller.")
        else:
            print(f"El vehículo {self.modelo} ({self.patente}) ya se encuentra en el taller.")

    def entregar(self):
        """Marca el vehículo como entregado al cliente."""
        if self.__en_taller:
            self.__en_taller = False
            print(f"El vehículo {self.modelo} ({self.patente}) ha sido entregado al cliente.")
        else:
            print(f"El vehículo {self.modelo} ({self.patente}) no está actualmente en el taller.")

    def tarifa_hora(self) -> float:
        """
        Devuelve la tarifa base por hora de reparación.
        """
        # Puedes modificar este valor o agregar lógica para que dependa del modelo o año.
        return 35.0  

    def __str__(self):
        estado = "En taller" if self.__en_taller else "Fuera del taller"
        return f"Vehículo [Patente: {self.patente}, Modelo: {self.modelo}, Año: {self.anio}, Estado: {estado}]"

# Código de prueba rápido
if __name__ == "__main__":
    mi_auto = Vehiculo(patente="AB123CD", modelo="Toyota Corolla", anio=2021)
    print(mi_auto)
    
    # Probando los métodos
    mi_auto.ingresar()
    print(f"La tarifa por hora de este vehículo es: ")
    mi_auto.entregar()
    
    print(mi_auto)
