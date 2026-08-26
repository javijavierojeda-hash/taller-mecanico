from vehiculo import Vehiculo

def main():
    print("=== Bienvenido al Sistema del Taller Mecánico ===")
    print("Registrando vehículos...\n")
    
    # 1. Crear 3 vehículos con sus respectivos atributos
    vehiculo1 = Vehiculo(patente="ABC-123", modelo="Toyota Yaris", anio=2020)
    vehiculo2 = Vehiculo(patente="XYZ-987", modelo="Honda Civic", anio=2018)
    vehiculo3 = Vehiculo(patente="DEF-456", modelo="Ford Ranger", anio=2022)

    # 2. Mostrar la información de los vehículos y su tarifa por hora
    print("--- Flota actual y Tarifas ---")
    print(vehiculo1)
    print(f"Tarifa por hora: ${vehiculo1.tarifa_hora()}\n")
    
    print(vehiculo2)
    print(f"Tarifa por hora: ${vehiculo2.tarifa_hora()}\n")
    
    print(vehiculo3)
    print(f"Tarifa por hora: ${vehiculo3.tarifa_hora()}\n")

    # 3. Simular alguna operación para probar los métodos
    print("--- Ingresando vehículos al taller ---")
    vehiculo1.ingresar()
    vehiculo2.ingresar()

if __name__ == "__main__":
    main()
