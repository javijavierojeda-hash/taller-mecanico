"""
Módulo con funciones auxiliares para solicitar y validar datos por consola.
Permite pedir información al usuario y reintentar automáticamente si hay errores de digitación.
"""

# Definimos una función para pedir un número entero con validación de tipo y rango
def pedir_entero(mensaje: str, minimo: int = None, maximo: int = None) -> int:
    # Mantenemos un bucle infinito hasta que el usuario ingrese un número válido
    while True:
        # Leemos la entrada del usuario y eliminamos espacios alrededor
        entrada = input(mensaje).strip()
        # Intentamos convertir la entrada a número entero
        try:
            valor = int(entrada)
        # Si la conversión falla (ingresó letras o símbolos), mostramos error y reintentamos
        except ValueError:
            print(f"  [ERROR] '{entrada}' no es un numero entero valido. Intentalo de nuevo.\n")
            continue

        # Si se definió un valor mínimo y el número ingresado es menor, avisamos al usuario
        if minimo is not None and valor < minimo:
            print(f"  [ERROR] El valor no puede ser menor a {minimo}. Intentalo de nuevo.\n")
            continue

        # Si se definió un valor máximo y el número ingresado es mayor, avisamos al usuario
        if maximo is not None and valor > maximo:
            print(f"  [ERROR] El valor no puede ser mayor a {maximo}. Intentalo de nuevo.\n")
            continue

        # Si superó todas las comprobaciones, retornamos el número entero válido
        return valor

# Definimos una función para solicitar un texto que no esté vacío y tenga largo mínimo
def pedir_texto(mensaje: str, longitud_minima: int = 2) -> str:
    # Mantenemos el bucle hasta recibir texto válido
    while True:
        # Leemos el texto ingresado por el usuario y quitamos espacios en los bordes
        entrada = input(mensaje).strip()
        # Validamos que no esté vacío y tenga la longitud requerida
        if not entrada or len(entrada) < longitud_minima:
            print(f"  [ERROR] El texto debe tener al menos {longitud_minima} caracteres y no estar vacio.\n")
            continue
        # Retornamos el texto válido
        return entrada

# Definimos una función especializada para solicitar una patente
def pedir_patente(mensaje: str = "Ingrese patente (minimo 6 caracteres, sin espacios): ") -> str:
    # Bucle de reintento interactivo
    while True:
        # Leemos la patente ingresada y limpiamos espacios alrededor
        patente = input(mensaje).strip()
        # Verificamos que tenga 6 o más caracteres y no contenga espacios intermedios
        if len(patente) < 6 or " " in patente:
            print(f"  [ERROR] La patente '{patente}' es invalida. Debe tener al menos 6 caracteres y no contener espacios.\n")
            continue
        # Mostramos confirmación de patente válida y la retornamos
        print(f"  [OK] Patente '{patente}' valida.")
        return patente

# Definimos una función para solicitar un año coherente de vehículo
def pedir_anio(mensaje: str = "Ingrese el año del vehiculo (1900 - 2030): ") -> int:
    # Reutilizamos pedir_entero fijando el rango de 1900 a 2030
    return pedir_entero(mensaje, minimo=1900, maximo=2030)
