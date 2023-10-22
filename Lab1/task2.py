def f(x):
    if x == 0:  # Handle the edge case
        return 0
    return 1 / (x * (x**2 + 1))**0.5

def trapezoidal_integration_adaptive(func, a, b, epsilon):
    def trapezoidal(func, a, b, n):
        h = (b - a) / n
        s = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            s += func(a + i*h)
        return s * h

    n = 1 
    integration_prev = trapezoidal(func, a, b, n)
    n *= 2
    k = 2
    integration_curr = trapezoidal(func, a, b, n)
    error = abs(integration_curr - integration_prev) / 3

    while error > epsilon:
        n *= 2  
        k +=1
        integration_prev = integration_curr
        integration_curr = trapezoidal(func, a, b, n)
        error = abs(integration_curr - integration_prev) / 3
        print(integration_prev,integration_curr)

    return integration_curr, k

a = 0.01
b = 1
epsilon = 0.3  

result, n_used = trapezoidal_integration_adaptive(f, a, b, epsilon)

print(f"Integration result: {result}")
print(f"Number of iterations: {n_used}")