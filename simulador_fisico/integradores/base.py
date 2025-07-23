from abc import ABC, abstractmethod

class Integrator(ABC):
    @abstractmethod
    def step(self, system_state, dt):
        pass

    def simular(self, estado_inicial, pasos, dt):
        trayectorias = [[(p.pos.copy(), p.vel.copy()) for p in estado_inicial.particulas]]
        estado = estado_inicial
        for _ in range(pasos):
            estado = self.step(estado, dt)
            trayectorias.append([(p.pos.copy(), p.vel.copy()) for p in estado.particulas])
        return [list(zip(*trayectorias))]
