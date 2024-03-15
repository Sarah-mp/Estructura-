def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    return fib_series

# Solicitar al usuario el número de términos de la serie de Fibonacci
num_terminos = int(input("Ingrese el número de términos de la serie de Fibonacci: "))

# Generar la serie de Fibonacci
serie_fibonacci = fibonacci(num_terminos)

# Imprimir la serie de Fibonacci
print("Serie de Fibonacci:")
for term in serie_fibonacci:
    print(term, end=" ")
