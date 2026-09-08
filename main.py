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
    # REQUISITO: Try con múltiples Except (ValueError y TypeError) + Finally
    # 1. Usamos el dato validable (property con setter) sobre Vehiculo
    # 2. Primer except: ValueError (valor o formato inválido)
    # 3. Segundo except: TypeError (tipo incorrecto, ej: número donde se espera texto)
    # 4. Cláusula finally: imprime mensaje de cierre (se ejecuta siempre)
    # 5. Confirmación de que el resto del programa sigue ejecutándose después
    # =========================================================================
    print("\n--- Demostración: Try / Except múltiple (ValueError + TypeError) + Finally ---")
    print("Probando asignar un tipo incorrecto (un número 123456 donde se esperaba texto en patente)...")
    try:
        # Pasamos un número (int) a una propiedad que espera texto (str)
        vehiculo1.patente = 123456
    except ValueError as e:
        # Primer except: captura valores con formato inválido
        print(f"   [AVISO - Error de Valor]: {e}")
    except TypeError as e:
        # Segundo except: captura tipos de datos incorrectos
        print(f"   [AVISO - Error de Tipo]: Se esperaba texto pero se recibio otro tipo -> {e}")
    finally:
        # Bloque finally: se ejecuta SIEMPRE, haya ocurrido o no un error
        print("   [FINALLY]: Finalizando bloque de validacion (este mensaje siempre se muestra).")

    # Confirmación de que el resto del programa sigue ejecutándose después
    print("   [CONFIRMACION]: El programa no exploto y el resto del codigo sigue ejecutandose con normalidad.\n")

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
