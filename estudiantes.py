# Función para calcular el promedio de edades
def calcular_promedio_edades(edades):
    total_edades = sum(edades)
    promedio = total_edades / len(edades)
    return promedio

# Ejemplo de uso del programa
num_hombres = int(input("Ingrese el número de hombres en el grupo: "))
edades_hombres = [int(input(f"Ingrese la edad del hombre {i + 1}: ")) for i in range(num_hombres)]

num_mujeres = int(input("Ingrese el número de mujeres en el grupo: "))
edades_mujeres = [int(input(f"Ingrese la edad de la mujer {i + 1}: ")) for i in range(num_mujeres)]

promedio_hombres = calcular_promedio_edades(edades_hombres)
promedio_mujeres = calcular_promedio_edades(edades_mujeres)

print(f"El promedio de edad de los hombres es: {promedio_hombres:.2f}")
print(f"El promedio de edad de las mujeres es: {promedio_mujeres:.2f}")