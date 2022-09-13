import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# Функция, которой описываются наши данные
# def func(x, a, b, c):
#     return a * np.exp(-b * x) + c
# def func(x, a, b, c):
#     return a*x*x+b*x+c
def func(x, a, b):
    return a*x+b

xdata = np.array([2, 3, 4, 6, 7, 9])
ydata = np.array([12, 15, 17, 19, 26, 35])
yerr = np.full(6, 10)
plt.plot(xdata, ydata, 'b.', label='input_data')
plt.errorbar(xdata, ydata, yerr=yerr, fmt='o', ecolor='red')

# params, _ = curve_fit(func, xdata, ydata) #[3.08133971 4.74641148]
# print(params)
# plt.plot(xdata, func(xdata, *params), 'r-', label='fitted curve')

# params2, _ = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
#plt.text(2, 35, f"k = {params[0]}\nb = {params[1]}")

p, v = np.polyfit(xdata, ydata, deg=1, cov=True)
print(p)
p_f = np.poly1d(p)
plt.plot(xdata, p_f(xdata), 'r-', label='fitted curve')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(which='both')
plt.legend()
plt.show()