from model.marca import Marca
from model.modelo import Modelo
from model.auto import Auto
from model.moto import Moto
from model.camion import Camion
from model.persona import Persona
from model.cliente import Cliente
from model.rol import Rol
from model.usuario import Usuario
from model.repuesto import Repuesto
from model.ordentrabajo import OrdenTrabajo

def main():
    # 1. Crear Marcas y Modelos
    marca_toyota = Marca("Toyota")
    modelo_yaris = Modelo("Yaris", marca_toyota)

    marca_honda = Marca("Honda")
    modelo_cbr = Modelo("CBR500R", marca_honda)

    marca_volvo = Marca("Volvo")
    modelo_fh = Modelo("FH16", marca_volvo)

    # 2. Instanciar Vehículos
    auto = Auto("AB1234", 2018, modelo_yaris)
    moto = Moto("CD5678", 2020, modelo_cbr)
    camion = Camion("EF9012", 2023, modelo_fh, 5000)

    # 3. Pruebas de ingreso al taller
    print("--- Ingreso de Vehículos ---")
    print(auto.ingresar())
    print(moto.ingresar())
    print(camion.ingresar())
    print()

    # 4. Pruebas de tarifas
    print("--- Tarifas por Hora ---")
    print(f"Tarifa Auto ({auto.modelo.marca.nombre} {auto.modelo.nombre}): ${auto.tarifa_hora()}")
    print(f"Tarifa Moto ({moto.modelo.marca.nombre} {moto.modelo.nombre}): ${moto.tarifa_hora()}")
    print(f"Tarifa Camión ({camion.modelo.marca.nombre} {camion.modelo.nombre}): ${camion.tarifa_hora()}")
    print()

    # 5. Crear Personas, Clientes y Usuarios
    persona_mecanico = Persona("12.345.678-9", "Juan Mecánico")
    rol_mecanico = Rol("Mecánico", ["reparar", "cerrar_orden"])
    usuario_mecanico = Usuario("juanm", "hash123", rol_mecanico, persona_mecanico)

    persona_cliente = Persona("9.876.543-2", "Pedro Cliente")
    cliente_pedro = Cliente(persona_cliente)

    # 6. Crear Orden de Trabajo
    print("--- Gestión de Orden de Trabajo ---")
    orden1 = OrdenTrabajo(1, "Cambio de aceite y pastillas", auto, usuario_mecanico)
    orden1.agregar_horas(3)
    
    # 7. Agregar Repuestos
    filtro = Repuesto("F-001", "Filtro de Aceite", 10, False)
    pastillas = Repuesto("P-002", "Pastillas de freno", 5, True)
    
    orden1.agregar_repuesto(1, 15000, filtro)
    orden1.agregar_repuesto(1, 45000, pastillas)
    
    # 8. Calcular Total y Cerrar
    print(f"Total de Orden #1 (Mano de obra + Repuestos): ${orden1.total()}")
    orden1.cerrar()
    print("Orden cerrada exitosamente.")

if __name__ == "__main__":
    main()
