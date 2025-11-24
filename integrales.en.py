# integral_plot.py
"""
Plot a mathematical function and compute the area under its curve
(using the trapezoidal rule).

Dependencies:
    numpy
    matplotlib

Install with:
    pip install numpy matplotlib
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def parse_function(expr: str):
    """
    Convert a string mathematical expression in x into a Python callable.
    For simplicity this uses eval—be careful with untrusted input.
    """
    def f(x):
        return eval(expr, {"x": x, "math": math, "np": np})
    return f

def trapezoidal_rule(f, a: float, b: float, n: int = 1000):
    """
    Approximate the integral of f(x) from a to b using the trapezoidal rule.
    
    :param f: function of one variable
    :param a: lower bound
    :param b: upper bound
    :param n: number of subdivisions (default = 1000)
    :return: approximate area
    """
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    area = (h/2) * np.sum(y[0:-1] + y[1:])
    return area

def plot_function_and_area(f, a: float, b: float, title: str = None):
    """
    Plot the function f(x) and highlight the area under the curve from a to b.
    """
    x_plot = np.linspace(a, b, 400)
    y_plot = f(x_plot)

    plt.figure(figsize=(8, 5))
    plt.plot(x_plot, y_plot, label="f(x)")
    plt.fill_between(x_plot, y_plot, where=(y_plot > 0), alpha=0.3, label="Area under curve")

    plt.axhline(0, color='black', linewidth=0.5)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    if title:
        plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    print("=== Function Plotter & Integral Calculator ===")
    expr = input("Enter a function in variable x (use math and/or np, e.g. ‘math.sin(x)’): ")
    f = parse_function(expr)
    
    a = float(input("Enter the lower bound a: "))
    b = float(input("Enter the upper bound b: "))
    n = int(input("Enter number of subdivisions (e.g. 1000): "))

    area = trapezoidal_rule(f, a, b, n)
    print(f"Approximate area under curve from {a} to {b}: {area:.6f}")

    plot_function_and_area(f, a, b, title=f"f(x) = {expr}")

if __name__ == "__main__":
    main()
