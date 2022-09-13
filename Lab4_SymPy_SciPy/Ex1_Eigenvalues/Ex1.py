from sympy import *
# A = np.zeros((9,9))
l = Symbol("l", positive = True)
m = Symbol("m", positive = True)
r = Symbol("r", positive = True)
i = Symbol("i", positive = True)
# A = Matrix([
#     [0, 0, 0, -1/r, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, -1/r, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, -1/r, 0, 0, 0],
#     [-l-2*m, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, -m, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, -m, 0, 0, 0, 0, 0, 0],
#     [-l, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [-l, 0, 0, 0, 0, 0, 0, 0, 0]]
# )
A = Matrix([[1+i, 2, 2],[0, -1+i, -2], [0, 1, 1+i]])
B = A.eigenvals()
print(B)
for (root, multiplicity) in B.items():#zip(B.keys(), B.values()):
    print(f"Root {root} with multiplicity {multiplicity}")

