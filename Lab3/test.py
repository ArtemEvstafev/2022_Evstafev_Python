from sympy import symbols, Eq, solve

x = symbols('x')

a = symbols('a')
f2 = x**2 + a * a * x
e2 = Eq(f2, 0)
result2_1 = solve(e2)
print(result2_1)