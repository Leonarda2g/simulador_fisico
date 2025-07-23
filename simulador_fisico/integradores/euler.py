from integradores.base import Integrator
from modelos.particula import Particula
from modelos.sistema import SystemState
import numpy as np


def aceleracion_gravitacional(pos):
    # Campo gravitacional central: a = -GM * r / |r|^3
    G = 1.0
    M = 10.0
    r = pos
    dist = np.linalg.norm(r)
    if dist == 0:
        return np.zeros_like(pos)
    return -G * M * r / dist**3


class EulerIntegrator(Integrator):
    def step(self, system_state, dt):
        nuevas_particulas = []
        for p in system_state.particulas:
            a = aceleracion_gravitacional(p.pos)
            nueva_vel = p.vel + dt * a
            nueva_pos = p.pos + dt * p.vel
            nuevas_particulas.append(Particula(nueva_pos, nueva_vel, p.masa))
        return SystemState(nuevas_particulas)