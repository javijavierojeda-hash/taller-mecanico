class Vehiculo:
    """
    Clase que representa un vehículo dentro del sistema del Taller Mecánico.
    """

    def __init__(self, patente: str, anio: int):
        """
        Constructor de la clase Vehiculo.
        
        Parámetros:
        - patente (str): La matrícula o placa del vehículo.
        - anio (int): El año de fabricación del vehículo.
        """
        self.patente = patente
        self.anio = anio

    def __str__(self):
        return f"Vehículo [Patente: {self.patente}, Año: {self.anio}]"

# Código de prueba rápido (se ejecuta si corres este archivo directamente)
if __name__ == "__main__":
    # Creamos un vehículo de ejemplo
    mi_auto = Vehiculo(patente="AB123CD", anio=2021)
    print("Vehículo creado exitosamente:")
    print(mi_auto)
