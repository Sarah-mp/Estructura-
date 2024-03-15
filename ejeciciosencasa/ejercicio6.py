def division_por_restas(dividendo, divisor):
    cociente = 0
    resto = dividendo
    
    for i in range(dividendo, 0, -divisor):
        resto -= divisor
        cociente += 1
    
    return cociente

# Ejemplo de uso:
dividendo = 20
divisor = 4
resultado = division_por_restas(dividendo, divisor)
print("Resultado de la división:", resultado)