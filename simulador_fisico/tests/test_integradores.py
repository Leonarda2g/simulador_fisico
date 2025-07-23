import numpy as np
import pytest

from modelos.particula import Particula
from modelos.sistema import SystemState
from integradores.euler import EulerIntegrator
from integradores.leapfrog import LeapfrogIntegrator
from integradores.rk8 import RK8Integrator
from integradores.bulirsch_stoer import BulirschStoerIntegrator

@pytest.mark.parametrize("Integrador", [
    EulerIntegrator,
    LeapfrogIntegrator,
    RK8Integrator,
    BulirschStoerIntegrator
])
def test_integrador_avanza(Integrador):
    p = Particula([1, 0], [0, 1])
    estado = SystemState([p])
    integrador = Integrador()
    nuevo_estado = integrador.step(estado, 0.01)

    # Verifica tipo y cantidad de partículas
    assert isinstance(nuevo_estado, SystemState)
    assert len(nuevo_estado.particulas) == 1

    # Verifica que haya algún cambio (avanza)
    assert not np.allclose(nuevo_estado.particulas[0].pos, estado.particulas[0].pos)
