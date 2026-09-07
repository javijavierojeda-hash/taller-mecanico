# Definimos la clase llamada 'Vehiculo', que sirve como plantilla para crear objetos de tipo auto
class Vehiculo:

    # El método __init__ es el constructor que inicializa los atributos al crear un nuevo vehículo
    def __init__(self, patente: str, modelo: str, anio: int):
        # Asignamos la patente a través del setter para que se ejecute la validación
        self.patente = patente
        # Asignamos el modelo a través del setter para validar que no esté vacío
        self.modelo = modelo
        # Asignamos el año a través del setter para validar formato y rango
        self.anio = anio
        # Creamos un atributo privado (usando __) que inicia en Falso porque el auto aún no ingresa
        self.__en_taller = False  

    # --- PROPIEDAD: PATENTE ---
    # Definimos el getter de la propiedad patente para acceder al atributo privado
    @property
    def patente(self) -> str:
        # Retorna el valor del atributo privado
        return self.__patente

    # Definimos el setter de la propiedad patente para validar el valor antes de asignarlo
    @patente.setter
    def patente(self, valor: str):
        # Validamos que tenga al menos 6 caracteres y no contenga espacios
        if not isinstance(valor, str) or len(valor) < 6 or " " in valor:
            print(f"  [ERROR DE VALIDACION] La patente '{valor}' no es valida (minimo 6 caracteres y sin espacios).")
            raise ValueError(
                f"Patente invalida: '{valor}'. Debe tener al menos 6 caracteres y no contener espacios."
            )
        # Asignamos el valor validado al atributo privado
        self.__patente = valor
        print(f"  [VALIDACION EXITOSA] Patente '{valor}' verificada y asignada correctamente.")

    # --- PROPIEDAD: MODELO ---
    # Definimos el getter de la propiedad modelo para acceder al atributo privado
    @property
    def modelo(self) -> str:
        # Retorna el valor del atributo privado
        return self.__modelo

    # Definimos el setter de la propiedad modelo para validar que no esté vacío
    @modelo.setter
    def modelo(self, valor: str):
        # Validamos que sea texto, no esté vacío y tenga al menos 2 caracteres
        if not isinstance(valor, str) or not valor.strip() or len(valor.strip()) < 2:
            print(f"  [ERROR DE VALIDACION] El modelo '{valor}' no es valido. Debe tener al menos 2 caracteres y no estar vacio.")
            raise ValueError(
                f"Modelo invalido: '{valor}'. Debe tener al menos 2 caracteres y no estar vacio."
            )
        # Guardamos el modelo limpio de espacios al inicio/final
        self.__modelo = valor.strip()
        print(f"  [VALIDACION EXITOSA] Modelo '{self.__modelo}' registrado correctamente.")

    # --- PROPIEDAD: ANIO ---
    # Definimos el getter de la propiedad anio para acceder al atributo privado
    @property
    def anio(self) -> int:
        # Retorna el valor del atributo privado
        return self.__anio

    # Definimos el setter de la propiedad anio para validar número entero y rango coherente
    @anio.setter
    def anio(self, valor: int):
        # Validamos que sea un número entero
        try:
            valor_int = int(valor)
        except (ValueError, TypeError):
            print(f"  [ERROR DE VALIDACION] El año '{valor}' no es valido. Debe ser un numero entero (ej: 2020).")
            raise ValueError(
                f"Año invalido: '{valor}'. Debe ser un numero entero."
            )

        # Validamos que esté dentro de un rango realista (1900 a 2030)
        if valor_int < 1900 or valor_int > 2030:
            print(f"  [ERROR DE VALIDACION] El año '{valor_int}' esta fuera del rango permitido (1900 - 2030).")
            raise ValueError(
                f"Año '{valor_int}' fuera de rango. Ingrese un año entre 1900 y 2030."
            )

        # Asignamos el valor validado al atributo privado
        self.__anio = valor_int
        print(f"  [VALIDACION EXITOSA] Año {valor_int} registrado correctamente.")

    # Definimos el método para registrar el ingreso del vehículo al taller
    def ingresar(self):
        # Comprobamos si el vehículo NO está en el taller
        if not self.__en_taller:
            # Cambiamos el estado a Verdadero porque acaba de ingresar
            self.__en_taller = True
            # Imprimimos un mensaje confirmando el ingreso exitoso
            print(f"El vehículo {self.modelo} ({self.patente}) ha ingresado al taller.")
        # Si ya estaba en el taller, se ejecuta el else
        else:
            # Imprimimos un mensaje avisando que ya está registrado adentro
            print(f"El vehículo {self.modelo} ({self.patente}) ya se encuentra en el taller.")

    # Definimos el método para devolver el vehículo al cliente
    def entregar(self):
        # Comprobamos si el vehículo efectivamente está en el taller (Verdadero)
        if self.__en_taller:
            # Cambiamos el estado a Falso porque ya se va del local
            self.__en_taller = False
            # Imprimimos un mensaje confirmando la entrega
            print(f"El vehículo {self.modelo} ({self.patente}) ha sido entregado al cliente.")
        # Si el auto no estaba en el local...
        else:
            # Avisamos que hay un error porque no se puede entregar algo que no está
            print(f"El vehículo {self.modelo} ({self.patente}) no está actualmente en el taller.")

    # Definimos un método que nos dirá cuánto cobra este vehículo por hora de trabajo
    def tarifa_hora(self) -> float:
        # Retorna el valor fijo de 35.0 (número con decimales o flotante)
        return 35.0  

    # El método especial __str__ define qué texto se muestra si usamos print() sobre el objeto
    def __str__(self):
        # Creamos un texto que diga 'En taller' si es Verdadero, o 'Fuera del taller' si es Falso
        estado = "En taller" if self.__en_taller else "Fuera del taller"
        # Devolvemos una cadena de texto (f-string) uniendo todos los datos del auto para mostrar
        return f"Vehículo [Patente: {self.patente}, Modelo: {self.modelo}, Año: {self.anio}, Estado: {estado}]"
