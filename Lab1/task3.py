import numpy as np
import scipy.integrate as integrate


def f(x):
    return np.exp(x)


def coefficient(n, x):
    coef = ((2**(n+1)* np.math.factorial(n) * np.sqrt(np.pi)))/((24*(x**2)-12)**2)
    return coef

def integral_approximation(n):
    herm_coef = [8, 0, -12, 0] 
    roots = np.roots(herm_coef)
    print("roots",roots)
    coefficients = [coefficient(n, r) for r in roots]
    print(coefficients)
    I_approx = sum([coeff * f(root) for coeff, root in zip(coefficients, roots)])
    
    return I_approx, Rf

n = 3
I_approx, Rf = integral_approximation(n)

print(f"I_approx = {I_approx}")
