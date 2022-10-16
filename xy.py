import numpy as np

from sympy import symbols, Eq, solve

x, y = symbols('x y')

eq1 = Eq(x + y -5, 0)
eq2 = Eq(x - y + 3, 0)

solve((eq1, eq2), (x, y))

sol_dict = solve((eq1,eq2), (x, y))
print(f'x = {sol_dict[x]}')
print(f'y = {sol_dict[y]}')

Tce, Tbd = symbols('Tce Tbd')

eq1=Eq(Tce * np.cos(np.radians(30)) - Tbd * np.cos(np.radians(45)))
print(eq1)

eq2=Eq(Tce * np.sin(np.radians(30)) + Tbd * np.sin(np.radians(45))-22)
print(eq2)

solve((eq1,eq2),(Tce, Tbd))

sol_dict = solve((eq1,eq2),(Tce, Tbd))
print(f'Tce = {sol_dict[Tce]}')
print(f'Tce = {sol_dict[Tbd]}')

