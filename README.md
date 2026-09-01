# 🚗 Sistema de Gestión - Taller Mecánico

Sistema en **Python** orientado a objetos para la gestión, registro e ingreso de vehículos en un taller mecánico utilizando conceptos de herencia y encapsulamiento.

---

## 📁 Estructura del Proyecto

```text
taller-mecanico/
├── .gitignore       # Archivos y carpetas ignorados por Git
├── auto.py          # Subclase Auto (con capacidad_maletero)
├── camion.py        # Subclase Camion (con capacidad_carga)
├── moto.py          # Subclase Moto (hereda de Vehiculo)
├── vehiculo.py      # Clase base Vehiculo y lógica general
├── main.py          # Archivo principal de ejecución y pruebas
└── README.md        # Documentación del proyecto
```

---

## ⚙️ Descripción de los Módulos

### 1. `vehiculo.py` (Clase Base `Vehiculo`)
Modela los datos y el comportamiento común de todos los vehículos del taller.

* **Atributos:**
  * `patente` *(str)*: Placa o patente identificatoria del vehículo.
  * `modelo` *(str)*: Marca y modelo.
  * `anio` *(int)*: Año de fabricación.
  * `__en_taller` *(bool, privado)*: Indica si el vehículo está en el taller (`True`) o fuera (`False`).

* **Métodos principales:**
  * `ingresar()`: Registra la entrada del vehículo al taller.
  * `entregar()`: Registra la salida/entrega del vehículo al cliente.
  * `tarifa_hora()`: Retorna la tarifa por hora de trabajo asignada (base: `$35.0`).
  * `__str__()`: Representación textual del vehículo y su estado actual.

---

### 2. Subclases (Herencia de `Vehiculo`)

* **`auto.py` (Clase `Auto`):**
  * Hereda todos los atributos y métodos de `Vehiculo`.
  * **Atributo propio:** `__capacidad_maletero` *(int, privado)*: Capacidad del baúl/maletero en litros.

* **`camion.py` (Clase `Camion`):**
  * Hereda todos los atributos y métodos de `Vehiculo`.
  * **Atributo propio:** `__capacidad_carga` *(int, privado)*: Capacidad de carga en kilogramos.

* **`moto.py` (Clase `Moto`):**
  * Hereda directamente todos los atributos y métodos de `Vehiculo`.

---

### 3. `main.py` (Punto de Entrada)
Programa principal que:
1. Instancia vehículos específicos utilizando las subclases (`Auto`, `Moto`, `Camion`).
2. Consulta e imprime la información de cada vehículo y sus tarifas horarias.
3. Simula el ingreso de los vehículos al taller con `ingresar()`.

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos:
* **Python 3.8+** instalado.

### Ejecución:
```bash
python main.py
```

### Salida esperada:
```text
=== Bienvenido al Sistema del Taller Mecánico ===
Registrando vehículos...

--- Flota actual y Tarifas ---
Vehículo [Patente: ABC-123, Modelo: Toyota Yaris, Año: 2020, Estado: Fuera del taller]
Tarifa por hora: $35.0

Vehículo [Patente: XYZ-987, Modelo: Honda CBR, Año: 2018, Estado: Fuera del taller]
Tarifa por hora: $35.0

Vehículo [Patente: DEF-456, Modelo: Ford Ranger, Año: 2022, Estado: Fuera del taller]
Tarifa por hora: $35.0

--- Ingresando vehículos al taller ---
El vehículo Toyota Yaris (ABC-123) ha ingresado al taller.
El vehículo Honda CBR (XYZ-987) ha ingresado al taller.
```

---

## 🌿 Control de Versiones y Ramas (Git & GitHub)

### Enlaces del Proyecto:
* **Repositorio principal:** [github.com/javijavierojeda-hash/taller-mecanico](https://github.com/javijavierojeda-hash/taller-mecanico)
* **Rama de desarrollo activa:** [`rama-taller-mecanico`](https://github.com/javijavierojeda-hash/taller-mecanico/tree/rama-taller-mecanico)
* **Pull Request:** [Crear / Ver Pull Request en GitHub](https://github.com/javijavierojeda-hash/taller-mecanico/pull/new/rama-taller-mecanico)

---

### 🛠️ Flujo de Trabajo Git:

1. **Clonar repositorio:**
   ```bash
   git clone https://github.com/javijavierojeda-hash/taller-mecanico.git
   ```

2. **Crear y cambiar a la rama de trabajo:**
   ```bash
   git checkout -b rama-taller-mecanico
   ```

3. **Guardar y confirmar cambios (Commit):**
   ```bash
   git add .
   git commit -m "mensaje descriptivo"
   ```

4. **Publicar y subir cambios a GitHub (Push):**
   ```bash
   git push -u origin rama-taller-mecanico
   ```


