import csv
from modelos.particula import Particula
from modelos.sistema import SystemState

def cargar_condiciones_iniciales(ruta):
    particulas = []
    with open(ruta, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pos = list(map(float, row[0:2]))
            vel = list(map(float, row[2:4]))
            particulas.append(Particula(pos, vel))
    return SystemState(particulas)
