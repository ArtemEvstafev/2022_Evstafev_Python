import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
f = open(f"large.txt", 'r')
data = [i.rstrip() for i in f.readlines()]
f.close()
N = int(data[0])
A = np.array([i.split() for i in data[1:N+1]], dtype=np.float64)
b = np.array(data[-1].split(), dtype=np.float64)
x = linalg.solve(A, b)

fig, ax = plt.subplots()
fig.set_figheight(7)
fig.set_figwidth(14)
ax.grid(True)

ax.bar(np.arange(x.size), x, width = 0.5)
plt.savefig("Result_large.png")
plt.show()

