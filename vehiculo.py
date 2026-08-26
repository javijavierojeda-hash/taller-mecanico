# Definimos la clase llamada 'Vehiculo', que sirve como plantilla para crear objetos de tipo auto
class Vehiculo:

    # El método __init__ es el constructor que inicializa los atributos al crear un nuevo vehículo
    def __init__(self, patente: str, modelo: str, anio: int):
        # Guardamos la patente recibida como un atributo público
        self.patente = patente
        # Guardamos el modelo recibido como un atributo público
        self.modelo = modelo
        # Guardamos el año recibido como un atributo público
        self.anio = anio
        # Creamos un atributo privado (usando __) que inicia en Falso porque el auto aún no ingresa
        self.__en_taller = False  

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
