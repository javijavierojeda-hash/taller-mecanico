# Importamos las clases necesarias
from vehiculo import Vehiculo
from auto import Auto
from moto import Moto
from camion import Camion

# Definimos la función principal que contendrá el inicio del programa
def main():
    # Imprimimos un texto de bienvenida al usuario
    print("=== Bienvenido al Sistema del Taller Mecánico ===")
    # Imprimimos un mensaje avisando el inicio del registro
    print("Registrando vehículos...\n")
    
    # 1. Instanciamos un Auto con su capacidad de maletero
    vehiculo1 = Auto(patente="ABC-123", modelo="Toyota Yaris", anio=2020, capacidad_maletero=350)
    # 2. Instanciamos una Moto
    vehiculo2 = Moto(patente="XYZ-987", modelo="Honda CBR", anio=2018)
    # 3. Instanciamos un Camion con su capacidad de carga
    vehiculo3 = Camion(patente="DEF-456", anio=2022, capacidad_carga=2500, modelo="Ford Ranger")

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
