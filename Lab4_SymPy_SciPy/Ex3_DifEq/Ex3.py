import numpy as np
from scipy.integrate import odeint
import sympy as sp
import matplotlib.pyplot as plt

#C помощью SciPy
def dydx(y, x):
    return -y * 2


x_sp = np.linspace(0, 10, 100)
y0 = 2 ** 0.5
y_sp = np.array(odeint(dydx, y0, x_sp)).ravel()

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(7)
fig.set_figwidth(14)
ax1.grid(True)
ax1.plot(x_sp, y_sp)
ax1.set_title("SciPy")

#C помощью Sympy
y = sp.Function("y")
x = sp.Symbol("x", positive=True)

diffeq = sp.Eq(y(x).diff(x) + 2 * y(x), 0)
result = sp.dsolve(diffeq, ics={y(0): y0}).rhs
f = sp.lambdify(x, result, 'numpy')

ax2.grid(True)
ax2.plot(x_sp, f(x_sp), 'r')
ax2.set_title("SymPy")

plt.savefig("Solved.png")
plt.show()
