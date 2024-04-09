# Solicitar al usuario que ingrese la cantidad de empleados
num_empleados = int(input("Ingrese la cantidad de empleados: "))

# Crear una lista para almacenar los sueldos de los empleados
sueldos = []

# Iterar sobre el número de empleados para ingresar sus sueldos
for i in range(num_empleados):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
    sueldos.append(sueldo)

# Calcular el sueldo promedio
sueldo_promedio = sum(sueldos) / num_empleados

# Mostrar el sueldo promedio
print(f"El sueldo promedio del grupo de empleados es: {sueldo_promedio}")