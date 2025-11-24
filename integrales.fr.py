from math import *
import matplotlib.pyplot as plt
import numpy as np

formule = input("Entrez la formule en fonction de x (ex: x**2 - 10*x + 26): ")

def f(x):
    return eval(formule)

n = int(input("Quel est le nombre d'itérations ? "))
a = float(input("Quel est l'abscisse minimum ? "))
b = float(input("Quel est l'abscisse maximale ? "))

h = (b - a) / n
aire_total = 0

x_vals = np.linspace(a, b, 500)
y_vals = [f(x) for x in x_vals]

for i in range(1, n + 1):
    x0 = a + (i - 1) * h
    x1 = a + i * h
    aire = ((f(x0) + f(x1)) * h) / 2
    aire_total += aire

print("Aire totale sous la courbe :", aire_total)

plt.plot(x_vals, y_vals, label=f"f(x) = {formule}", color='blue')
plt.fill_between(x_vals, y_vals, alpha=0.2, color='red', label="Aire sous la courbe")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Représentation graphique de la fonction et aire sous la courbe")
plt.grid(True)
plt.legend()
plt.show()
