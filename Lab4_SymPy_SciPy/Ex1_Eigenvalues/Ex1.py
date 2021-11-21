from sympy import *
# A = np.zeros((9,9))
l = Symbol("l", positive = True)
m = Symbol("m", positive = True)
r = Symbol("r", positive = True)
A = Matrix([
    [0, 0, 0, -1/r, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1/r, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1/r, 0, 0, 0],
    [-l-2*m, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -m, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -m, 0, 0, 0, 0, 0, 0],
    [-l, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-l, 0, 0, 0, 0, 0, 0, 0, 0]]
)
B = A.eigenvals()

for (root, multiplicity) in B.items():#zip(B.keys(), B.values()):
    print(f"Root {root} with multiplicity {multiplicity}")

