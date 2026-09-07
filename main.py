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

    # Demostramos las validaciones de patente (éxito y error)
    print("\n--- Pruebas de validación de patente ---")

    # Caso 1: Patente inválida con espacios
    print("1. Probando patente con espacios ('AB 12 34'):")
    try:
        vehiculo1.patente = "AB 12 34"
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    # Caso 2: Patente inválida muy corta
    print("2. Probando patente muy corta ('A1'):")
    try:
        vehiculo1.patente = "A1"
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    # Caso 3: Patente válida
    print("3. Probando patente válida ('NUEVA-99'):")
    try:
        vehiculo1.patente = "NUEVA-99"
        print(f"   Nueva patente registrada en el objeto: {vehiculo1.patente}\n")
    except ValueError as e:
        print(f"   [Error]: {e}\n")

    # Demostramos las validaciones de año
    print("--- Pruebas de validación de año ---")
    print("1. Probando año fuera de rango (1850):")
    try:
        vehiculo1.anio = 1850
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    print("2. Probando año con formato incorrecto ('dos_mil'):")
    try:
        vehiculo1.anio = "dos_mil"
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    print("3. Probando año válido (2023):")
    try:
        vehiculo1.anio = 2023
        print(f"   Nuevo año registrado en el objeto: {vehiculo1.anio}\n")
    except ValueError as e:
        print(f"   [Error]: {e}\n")

    # Demostramos las validaciones de modelo
    print("--- Pruebas de validación de modelo ---")
    print("1. Probando modelo vacío o con espacios ('   '):")
    try:
        vehiculo1.modelo = "   "
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    print("2. Probando modelo válido ('Toyota Corolla Cross'):")
    try:
        vehiculo1.modelo = "Toyota Corolla Cross"
        print(f"   Nuevo modelo registrado: {vehiculo1.modelo}\n")
    except ValueError as e:
        print(f"   [Error]: {e}\n")

    # Demostramos las validaciones de capacidad de maletero y carga
    print("--- Pruebas de validación de capacidades ---")
    print("1. Probando capacidad de maletero negativa (-50 L):")
    try:
        vehiculo1.capacidad_maletero = -50
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    print("2. Probando capacidad de carga de camión inválida (0 kg):")
    try:
        vehiculo3.capacidad_carga = 0
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

# Condición especial de Python: comprueba si este es el archivo principal que se está ejecutando
if __name__ == "__main__":
    # Si es el archivo principal, ejecuta la función main()
    main()
