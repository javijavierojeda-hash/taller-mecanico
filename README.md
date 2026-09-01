# 🚗 Sistema de Gestión - Taller Mecánico

Sistema básico en **Python** orientado a objetos para la gestión, registro e ingreso de vehículos en un taller mecánico.

---

## 📁 Estructura del Proyecto

```text
taller-mecanico/
├── main.py          # Archivo principal de ejecución y pruebas
├── vehiculo.py      # Definición de la clase Vehiculo y su lógica
└── README.md        # Documentación del proyecto
```

---

## ⚙️ Descripción de los Módulos

### 1. `vehiculo.py` (Clase `Vehiculo`)
Modela los datos y el comportamiento de cada vehículo que llega al taller.

* **Atributos:**
  * `patente` *(str)*: Placa o patente identificatoria del vehículo.
  * `modelo` *(str)*: Marca y modelo (ej. *Toyota Yaris*).
  * `anio` *(int)*: Año de fabricación.
  * `__en_taller` *(bool, privado)*: Indica si el vehículo se encuentra dentro del taller (`True`) o fuera (`False`).

* **Métodos:**
  * `ingresar()`: Registra la entrada del vehículo al taller.
  * `entregar()`: Registra la salida/entrega del vehículo al cliente.
  * `tarifa_hora()`: Retorna la tarifa por hora de trabajo asignada (base: `$35.0`).
  * `__str__()`: Muestra una representación textual detallada del estado del vehículo.

---

### 2. `main.py` (Punto de Entrada)
Programa principal que:
1. Crea instancias de prueba para diferentes vehículos (*Toyota Yaris*, *Honda Civic*, *Ford Ranger*).
2. Consulta e imprime la flota y sus respectivas tarifas horarias.
3. Simula el ingreso de autos al taller con `ingresar()`.

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos:
* **Python 3.8+** instalado.

### Ejecución:
```bash
python main.py
```

---

## 🌿 Control de Versiones y Ramas (Git & GitHub)

### Enlaces del Proyecto:
* **Repositorio principal:** [github.com/javijavierojeda-hash/taller-mecanico](https://github.com/javijavierojeda-hash/taller-mecanico)
* **Rama de desarrollo activa:** [`rama-taller-mecanico`](https://github.com/javijavierojeda-hash/taller-mecanico/tree/rama-taller-mecanico)
* **Pull Request:** [Crear / Ver Pull Request en GitHub](https://github.com/javijavierojeda-hash/taller-mecanico/pull/new/rama-taller-mecanico)

---

### 🛠️ Comandos Git utilizados paso a paso:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/javijavierojeda-hash/taller-mecanico.git
   ```

2. **Crear y posicionarse en la nueva rama (`rama-taller-mecanico`):**
   ```bash
   git checkout -b rama-taller-mecanico
   ```

3. **Subir la rama a GitHub y vincular el seguimiento:**
   ```bash
   git push -u origin rama-taller-mecanico
   ```

4. **Comprobar en qué rama estás y el estado de los archivos:**
   ```bash
   git branch
   git status
   ```

