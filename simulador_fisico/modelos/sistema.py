class SystemState:
    def __init__(self, particulas):
        self.particulas = particulas

    def __repr__(self):
        return f"SystemState({len(self.particulas)} partículas)"
