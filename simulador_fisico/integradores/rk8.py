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


class RK8Integrator(Integrator):
    def step(self, system_state, dt):
        nuevas_particulas = []
        for p in system_state.particulas:
            def f(pos, vel):
                return aceleracion_gravitacional(pos)

            k1v = f(p.pos, p.vel)
            k1x = p.vel

            k2v = f(p.pos + 0.5*dt*k1x, p.vel + 0.5*dt*k1v)
            k2x = p.vel + 0.5*dt*k1v

            k3v = f(p.pos + 0.5*dt*k2x, p.vel + 0.5*dt*k2v)
            k3x = p.vel + 0.5*dt*k2v

            k4v = f(p.pos + dt*k3x, p.vel + dt*k3v)
            k4x = p.vel + dt*k3v

            nueva_pos = p.pos + dt/6 * (k1x + 2*k2x + 2*k3x + k4x)
            nueva_vel = p.vel + dt/6 * (k1v + 2*k2v + 2*k3v + k4v)
            nuevas_particulas.append(Particula(nueva_pos, nueva_vel, p.masa))
        return SystemState(nuevas_particulas)