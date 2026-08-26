from vehiculo import Vehiculo

def main():
    print("=== Bienvenido al Sistema del Taller Mecánico ===")
    print("Registrando vehículos...\n")
    
    # 1. Crear 3 vehículos con sus respectivos atributos
    vehiculo1 = Vehiculo(patente="ABC-123", modelo="Toyota Yaris", anio=2020)
    vehiculo2 = Vehiculo(patente="XYZ-987", modelo="Honda Civic", anio=2018)
    vehiculo3 = Vehiculo(patente="DEF-456", modelo="Ford Ranger", anio=2022)

    # 2. Mostrar la información de los vehículos creados
    print("--- Flota actual ---")
    print(vehiculo1)
    print(vehiculo2)
    print(vehiculo3)

    # 3. Simular alguna operación para probar los métodos
    print("\n--- Ingresando vehículos al taller ---")
    vehiculo1.ingresar()
    vehiculo2.ingresar()

if __name__ == "__main__":
    main()
