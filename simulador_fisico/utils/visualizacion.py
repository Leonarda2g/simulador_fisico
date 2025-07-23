import matplotlib.pyplot as plt
import matplotlib.animation as animation

def graficar_trayectorias(trayectorias, etiquetas):
    fig, ax = plt.subplots()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid()

    # Fijar el marco centrado en (0,0) con rango [-10, 10]
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    num_particulas = len(trayectorias[0])
    num_frames = len(trayectorias[0][0])

    # Crear líneas para cada partícula de cada integrador
    lines = []
    for tray, etiqueta in zip(trayectorias, etiquetas):
        for i, part in enumerate(tray):
            (line,) = ax.plot([], [], label=f"{etiqueta} - Partícula {i}")
            lines.append(line)

    ax.legend()

    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    def update(frame):
        for idx, tray in enumerate(trayectorias):
            for j, part in enumerate(tray):
                xs = [p[0][0] for p in part[:frame+1]]
                ys = [p[0][1] for p in part[:frame+1]]
                lines[idx * num_particulas + j].set_data(xs, ys)
        return lines

    ani = animation.FuncAnimation(
        fig, update, frames=num_frames, init_func=init,
        interval=30, blit=True, repeat=False
    )

    plt.show()
