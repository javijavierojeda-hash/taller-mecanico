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

    # =========================================================================
    # REQUISITO: Manejo de excepciones con Try / Except en dato validable
    # 1. Usamos el dato validable (property 'anio' con setter) sobre Vehiculo
    # 2. Probamos asignar un valor inválido dentro de un bloque try
    # 3. En el except capturamos el ValueError y mostramos un mensaje entendible
    # 4. Confirmamos que el resto del programa sigue ejecutándose después
    # =========================================================================
    print("\n--- Demostración: Prueba de dato validable con Try / Except ---")
    print("Intentando asignar un año inválido (1850) a vehiculo1...")
    try:
        vehiculo1.anio = 1850  # El setter de Vehiculo valida 1900-2030 y lanza ValueError
    except ValueError as e:
        # Imprimimos un mensaje amigable y entendible en vez de dejar que el programa explote
        print(f"   [AVISO - Error controlado]: No se pudo asignar el anio. Motivo: {e}")

    # 4. Confirmación explícita de que el resto del programa sigue ejecutándose
    print("   [CONFIRMACION]: El programa no exploto y el resto del codigo sigue ejecutandose.\n")

    # Demostramos más validaciones sobre otros atributos (patente, modelo, capacidades)
    print("--- Otras pruebas de validación complementarias ---")

    # Prueba de patente inválida y válida
    print("1. Probando patente inválida con espacios ('AB 12 34'):")
    try:
        vehiculo1.patente = "AB 12 34"
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    print("2. Probando patente válida ('NUEVA-99'):")
    try:
        vehiculo1.patente = "NUEVA-99"
        print(f"   Nueva patente registrada en el objeto: {vehiculo1.patente}\n")
    except ValueError as e:
        print(f"   [Error]: {e}\n")

    # Prueba de modelo inválido y válido
    print("3. Probando modelo vacío ('   '):")
    try:
        vehiculo1.modelo = "   "
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    print("4. Probando modelo válido ('Toyota Corolla Cross'):")
    try:
        vehiculo1.modelo = "Toyota Corolla Cross"
        print(f"   Nuevo modelo registrado: {vehiculo1.modelo}\n")
    except ValueError as e:
        print(f"   [Error]: {e}\n")

    # Demostramos las validaciones de capacidad de maletero y carga
    print("5. Probando capacidad de maletero negativa (-50 L):")
    try:
        vehiculo1.capacidad_maletero = -50
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    print("6. Probando capacidad de carga de camión inválida (0 kg):")
    try:
        vehiculo3.capacidad_carga = 0
    except ValueError as e:
        print(f"   [Excepción capturada]: {e}\n")

    print("=== Fin de la ejecución: Todo el programa se ejecutó exitosamente ===")

# Condición especial de Python: comprueba si este es el archivo principal que se está ejecutando
if __name__ == "__main__":
    # Si es el archivo principal, ejecuta la función main()
    main()
