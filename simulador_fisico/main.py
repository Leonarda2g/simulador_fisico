from utils.io import cargar_condiciones_iniciales
from utils.visualizacion import graficar_trayectorias
from integradores.euler import EulerIntegrator
from integradores.leapfrog import LeapfrogIntegrator
from integradores.rk8 import RK8Integrator
from integradores.bulirsch_stoer import BulirschStoerIntegrator

def seleccionar_metodo(nombre):
    metodos = {
        "euler": EulerIntegrator,
        "leapfrog": LeapfrogIntegrator,
        "rk8": RK8Integrator,
        "bulirschstoer": BulirschStoerIntegrator
    }
    nombre = nombre.lower()
    if nombre not in metodos:
        raise ValueError("Método no válido.")
    return metodos[nombre]()

def main():
    archivo = input("Ruta del archivo CSV con condiciones iniciales: ")
    metodo_nombre = input("Método de integración (euler, leapfrog, rk8, bulirschstoer): ")
    pasos = int(input("Número de pasos: "))
    dt = float(input("Valor de delta t: "))

    estado_inicial = cargar_condiciones_iniciales(archivo)
    integrador = seleccionar_metodo(metodo_nombre)
    trayectorias = integrador.simular(estado_inicial, pasos, dt)
    graficar_trayectorias(trayectorias, [metodo_nombre])

if __name__ == "__main__":
    main()