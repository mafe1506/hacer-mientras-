# Función para calcular el gasto anual
def calcular_gasto_anual(costo_mensual):
    return costo_mensual * 12

# Función para mostrar el gasto mensual
def mostrar_gasto_mensual(costo_mensual):
    print(f"El gasto mensual es de ${costo_mensual}")

# Costo mensual del servicio público
costo_mensual_electricidad = 100  # Ejemplo de costo mensual de electricidad

# Cálculo del gasto anual
gasto_anual_electricidad = calcular_gasto_anual(costo_mensual_electricidad)
print(f"El gasto anual de electricidad es de ${gasto_anual_electricidad}")

# Mostrar el gasto mensual
mostrar_gasto_mensual(costo_mensual_electricidad)