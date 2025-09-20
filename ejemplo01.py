import sympy as sp

# Definir variables
x, y, z = sp.symbols('x y z')

# Definir el sistema
f1 = x**2 + y + z - 4
f2 = x + y**2 + z - 5
f3 = x + y + z**2 - 6

# Resolver sistema no lineal
sol = sp.solve([f1, f2, f3], (x, y, z), dict=True)

print("Soluciones:")
for s in sol:
    print(s) 
