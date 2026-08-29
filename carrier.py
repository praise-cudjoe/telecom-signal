import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 1, 1000)
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 0.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)
ax.set_title("Square Wave Carrier Signal - 5Hz")

def animate(k):
    sine = np.sin(2 * np.pi * 5 * t + k/10)
    square = np.where(sine >= 0, 1, -1)
    line.set_data(t, square)
    return line,

ani = FuncAnimation(fig, animate, frames=200, interval=50)
plt.show()