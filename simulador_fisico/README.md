# Simulador de Evolución Temporal de Sistemas Físicos

Este proyecto permite simular la evolución de un sistema de partículas bajo diferentes métodos de integración numérica.

## Estructura básica
- Definición de partículas y estados del sistema.
- Integradores modulares.
- Método de Euler implementado.
- Método de Leapfrog implementado.
- Método de RK-8 implementado.
- Método de Burlisch-Stoer implementado.
- Entrada desde archivo `.csv`.
- Visualización 2D de trayectorias.

## Instalación
```bash
pip install -r requirements.txt
```

## Formato del archivo CSV
```
x, y, vx, vy
```
Cada fila representa una partícula.

## Ejecución
```bash
python main.py
```
