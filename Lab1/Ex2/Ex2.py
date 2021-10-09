import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(i):
    plt.title(f'Frame {i + 1}')
    line.set_ydata([float(i) for i in a[1 + 2 * i].split()])
    return line,


def decorations():
    fig.set_figheight(7)
    fig.set_figwidth(14)
    ax.axis([0, 17, -12, 12])
    ax.set_xticks(range(0, 17))
    ax.set_yticks(range(-12, 12))
    plt.xlabel('X')
    plt.ylabel('Y')
    ax.grid(True)


frame = 0
f = open(f"frames.dat.txt", 'r')
a = [i.rstrip() for i in f.readlines()]
f.close()

fig, ax = plt.subplots()
decorations()
x = [float(i) for i in a[0].split()]
y = [float(i) for i in a[1].split()]
line, = ax.plot(x, y)

ani = animation.FuncAnimation(
    fig, animate, interval=700, blit=False, frames=6)

ani.save("plot.gif")
