# Inicializar el número x y la potencia de 2
x = 1
potencia = 1

# Mientras la potencia sea menor o igual a 100, mostrar la potencia de 2 de x
while potencia <= 100:
    print(f"2^{x} = {potencia}")
    x += 1
    potencia = 2 ** x