import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

f = open(f"start.dat.txt", 'r')
y = np.array([i.rstrip() for i in f.readlines()], dtype=np.float64)
f.close()
x = np.arange(y.size)
b = np.zeros(y.size)

A = np.eye(y.size)
A[0][-1] = -1
B = np.vstack((b, np.eye(y.size)))[:-1,:]
A = A - B

fig, ax = plt.subplots()

fig.set_figheight(7)
fig.set_figwidth(14)
plt.xlabel('X')
plt.ylabel('Y')
ax.grid(True)

line, = ax.plot(x, y)

def animate(i):
    global y
    y = y - ((0.5 * A) @ y)
    line.set_ydata(y)
    return line,

ani = animation.FuncAnimation(
    fig, animate, interval=10, blit=False, frames=255, repeat=False)

ani.save("plot.gif", writer='pillow', fps=60)