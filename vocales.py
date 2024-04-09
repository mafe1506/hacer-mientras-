# Inicializar contadores para vocales y consonantes
vocales = 0
consonantes = 0

# Iterar para ingresar 10 letras
for _ in range(10):
    letra = input("Ingrese una letra: ").lower()  # Convertir la letra a minúscula para simplificar la comparación
    if letra.isalpha() and len(letra) == 1:  # Verificar que la entrada sea una sola letra del alfabeto
        if letra in "aeiou":  # Verificar si es vocal
            vocales += 1
        else:
            consonantes += 1

# Mostrar el recuento de vocales y consonantes ingresadas
print(f"Se ingresaron {vocales} vocales y {consonantes} consonantes.")