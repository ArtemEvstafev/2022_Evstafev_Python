
import numpy as np
import matplotlib.pyplot as plt
import math

# #f2 = np.array(list(map(float, input().split())))#берет вводимые значения и делает из них вектор
# U = np.array([26.67, 26.8, 27.1, 27.5, 28.3, 29.3, 31.8, 32.1])
# I = np.array([5.72, 4, 3.44, 2.84, 2.4, 2.08, 1.44, 0.4])
# file = open('PLAYERS.txt', 'w')
# for i in range(0,7):
#     print(f"{I[i]} {U[i]}", file=file)
# file.close()
# plt.plot(I, U)
# plt.show()

E1 = 1.63
E2 = 5.31
delE = E2 - E1

l = 6.6e-34*pow(5, 0.5) / pow(32*9.1e-31*(delE)*1.6e-19,0.5)
U = (0.8*E2 - 1.8*E1)# * 1.6e-19

n = 3
E = (pow(n * 6.6e-34 / 2 / 3.26e-10, 2) / 2 / 9.1e-31 - 2.03*1.6e-19) / 1.6e-19

Eq = pow(n * 6.6e-34 / 2, 2) / 2 / 9.1e-31 / pow(3.26e-10, 3) * 3.6e-10 / 100
print(l,'\n',U)
print('\n', Eq)
#f1 = np.array([1501, 2354, 2573, 2786])
#print(f1-655)