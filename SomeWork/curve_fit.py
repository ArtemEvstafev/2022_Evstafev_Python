import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

WS = pd.read_excel('data/451.xlsx')


# Функция, которой описываются наши данные
# def func(x, a, b, c):
#     return a * np.exp(-b * x) + c
# def func(x, a, b, c):
#     return a*x*x + b*x + c
def func(x, a, b):
    return a * x + b


# def func(x, a, b):
#     return a/x + b

def polyapprox():
    # Аппроксимация с помощью NUMPY POLYFIT
    p, v = np.polyfit(xdata, ydata, deg=1, cov=True)
    print(p)
    p_f = np.poly1d(p)
    plt.plot(xdata, p_f(xdata), 'r-', label='fitted curve')


def approx():
    # Аппроксимация с помощью SCIPY
    params, errors = curve_fit(func, xdata, ydata)
    print(params, '\n', np.sqrt(np.diag(errors)))
    # xcurve = np.linspace(xdata[0], xdata[-1], 100)
    xcurve = xdata
    plt.plot(xcurve, func(xcurve, *params), 'r-', label='fitted curve')

    # Если нужны границы
    # params2, _ = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
    # plt.text(2, 35, f"k = {params[0]}\nb = {params[1]}")
    plt.legend()


def theory():
    xcurve = np.linspace(xdata[0], xdata[-1], 100)
    ycurve = xcurve / (1. + 2 * xcurve / 511)
    plt.plot(xcurve, ycurve, 'r-', label='theoretical curve')


####################DATA WORKSPACE##########################
datax = np.array(WS["Channel"])
datay = np.array(WS["Counts"])


def kolibr(i):
    return 0.85 * i - 12.7


E = np.array([617.99, 1522.04, 798.64, 1410.64, 1598.42, 215.45, 302.65, 420.12])
delE = np.array([43.80, 75.74, 50.86, 68.45, 77.57, 9.59, 15.13, 18.50, 33.92])
time = WS.loc[0, 'Стенд N 3']
R = np.array([0.07, 0.05, 0.06, 0.05, 0.05, 0.07, 0.06, 0.08])

xdata = kolibr(datax)
ydata = datay / time

xerr = 0
yerr = 0
# yerr = np.zeros(len(ydata))
# xerr = np.zeros(len(ydata))

plt.ylabel('Энергия в кэВ')
plt.xlabel('Частиц в секунду')

# [print('%.2f' % i) for i in ydata]
############################################################

plt.errorbar(xdata, ydata, xerr=xerr, yerr=yerr, label='experimental data', fmt='o', ecolor='black', color='black',
             markersize=1,
             linewidth=0.5)

# theory()
# approx()


# beaty
plt.grid(which='major', color='black', linewidth=1, alpha=0.4)
plt.grid(which='minor', color='r', linestyle=':', linewidth=1, alpha=0.3)
plt.minorticks_on()

# plt.show()
plt.savefig("test.png", dpi=256)
