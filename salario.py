# Lista de salarios mensuales de los 20 empleados
salarios = [2500, 2700, 3000, 3200, 2800, 2600, 2900, 3100, 3300, 2750,
            2950, 2850, 3250, 3350, 2800, 3000, 3100, 2950, 2850, 3050]

# Función para calcular el salario con incremento del 2.5%
def calcular_salario_con_incremento(salario):
    return salario * (1 + 0.025)

# Calcular y mostrar el salario mensual de cada empleado con incremento del 2.5%
for i in range(len(salarios)):
    salario_con_incremento = calcular_salario_con_incremento(salarios[i])
    print(f"El salario mensual del empleado {i+1} es de ${salario_con_incremento:.2f}")

# Calcular el promedio de los salarios
promedio_salarios = sum(salarios) / len(salarios)
print(f"\nEl promedio de los salarios mensuales es de ${promedio_salarios:.2f}")