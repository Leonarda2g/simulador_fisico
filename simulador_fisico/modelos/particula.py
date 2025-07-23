import numpy as np

class Particula:
    def __init__(self, pos, vel, masa=1.0):
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.masa = masa

    def __repr__(self):
        return f"Particula(pos={self.pos}, vel={self.vel}, masa={self.masa})"
