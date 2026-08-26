# Importamos la clase Vehiculo desde el archivo vehiculo.py para poder usarla aquí
from vehiculo import Vehiculo

# Definimos la función principal que contendrá el inicio del programa
def main():
    # Imprimimos un texto de bienvenida al usuario
    print("=== Bienvenido al Sistema del Taller Mecánico ===")
    # Imprimimos un mensaje avisando el inicio del registro
    print("Registrando vehículos...\n")
    
    # 1. Creamos el primer objeto Vehiculo pasándole sus datos al constructor
    vehiculo1 = Vehiculo(patente="ABC-123", modelo="Toyota Yaris", anio=2020)
    # Creamos un segundo vehículo distinto
    vehiculo2 = Vehiculo(patente="XYZ-987", modelo="Honda Civic", anio=2018)
    # Creamos el tercer vehículo
    vehiculo3 = Vehiculo(patente="DEF-456", modelo="Ford Ranger", anio=2022)

    # Imprimimos un título para la lista de autos
    print("--- Flota actual y Tarifas ---")
    
    # Imprimimos toda la información del primer vehículo (esto ejecuta el __str__)
    print(vehiculo1)
    # Imprimimos la tarifa usando el método tarifa_hora()
    print(f"Tarifa por hora: ${vehiculo1.tarifa_hora()}\n")
    
    # Repetimos la impresión de información para el segundo vehículo
    print(vehiculo2)
    print(f"Tarifa por hora: ${vehiculo2.tarifa_hora()}\n")
    
    # Repetimos la impresión de información para el tercer vehículo
    print(vehiculo3)
    print(f"Tarifa por hora: ${vehiculo3.tarifa_hora()}\n")

    # Avisamos que comenzaremos a ingresar los autos al taller
    print("--- Ingresando vehículos al taller ---")
    # Ejecutamos el método ingresar() para que el primer vehículo cambie su estado y muestre mensaje
    vehiculo1.ingresar()
    # Ejecutamos el método ingresar() para el segundo vehículo
    vehiculo2.ingresar()

# Condición especial de Python: comprueba si este es el archivo principal que se está ejecutando
if __name__ == "__main__":
    # Si es el archivo principal, ejecuta la función main()
    main()
