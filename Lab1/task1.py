import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return -np.log(np.cos(x))

def get_real_values():
    points = np.arange(0, np.pi/2 + np.pi/36, np.pi/36)
    integral_values = []
    for upper_limit in points:
        value, _ = quad(f, 0, upper_limit)
        integral_values.append(value)
    return integral_values

def simpsons_rule(f, a, b, h):
    n = int((b - a) / h)
    result = f(a)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        result += 2 * f(a + i * h)
    result += f(b)
    result *= (h / 3)
    return result

def adaptive_simpsons(f, a, b, p):
    h = (b - a) / 2
    I_prev = simpsons_rule(f, a, b, h * 2)  
    I_curr = simpsons_rule(f, a, b, h)  
    error = abs((I_prev - I_curr) / (2**p-1))
    if (I_curr>1): epsilon =10e-7
    else: epsilon = get_precision_by_digits(I_curr, p)

    while error > epsilon:
        h /= 2
        I_prev = I_curr
        I_curr = simpsons_rule(f, a, b, h)
        error = abs((I_prev - I_curr) / (2**p-1))
    return I_curr, error


def get_precision_by_digits(approximate_result, digits):
    power = power_of_first_nonzero_digit(approximate_result)
    epsilon = 10**(power-digits)
    epsilon /= 2
    return epsilon

def power_of_first_nonzero_digit(number):
    num_str = str(number)
    found_digit = '0'
    for digit in num_str:
        if digit != '0' and digit != '.':
            found_digit = digit
            break
    first_digit_index = num_str.index(found_digit)
    point_index = 0
    try:point_index = num_str.index('.')
    except:point_index = len(num_str)
    return point_index - first_digit_index


def task():
    real_values = get_real_values()
    a, b, step = 0, np.pi / 2, np.pi/36
    points = np.arange(a, b + step, step)
    precision_digits = 4

    I_calc = []
    diffs = []

    for i, x in enumerate(points):
        if x == 0:
            I = real_values[0]
        else:
            I, _ = adaptive_simpsons(f, a, x, precision_digits)

        I_calc.append(I)
        diff = real_values[i] - I
        diffs.append(diff)


    df = pd.DataFrame({
    'X': [f'{p:.5f}' for p in points],
    'Estimated value': [f'{e:.10f}' for e in I_calc],
    'Real value': [f'{r:.10f}' for r in real_values],
    'Difference': [f'{d:.10f}' for d in diffs]
    })

    print(df)

    plt.figure(figsize=(10, 6))
    plt.plot(points, real_values, label='Real Values', color='blue')
    plt.plot(points, I_calc, label='Estimated Values', linestyle='dashed', color='red')
    plt.plot(points, diffs, label='Difference (Real - Estimated)', linestyle='dotted', color='green')
    plt.title('Lobachevskys Function: real values and estimation (using Simpson formula)')
    plt.xlabel('x')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()


task()



