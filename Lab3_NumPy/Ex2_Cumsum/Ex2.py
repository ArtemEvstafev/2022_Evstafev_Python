import matplotlib.pyplot as plt
import numpy as np
n = 9
for i in range(1,4):
    f = open(f"signals/signal0{i}.dat", 'r')
    y = np.array([i.rstrip() for i in f.readlines()], dtype=np.float64)
    x = np.arange(100)
    f.close()

    print(y)
    ret = np.cumsum(y, dtype=np.float64)
    ret[n:] = ret[n:] - ret[:-n]
    ret[n:] = ret[n:] / n
    for j in range(0, n):
        ret[j] /= j+1
    y_sum = ret
    print(y_sum)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figheight(9)
    fig.set_figwidth(18)
    ax1.set_title('До фильтра')
    ax2.set_title('После фильтра')
    ax1.plot(x, y)
    ax1.grid()
    ax2.plot(x, y_sum)
    ax2.grid()
    plt.savefig(f'better{i}.png')