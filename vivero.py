# Función para calcular el precio actualizado
def calcular_precio_actualizado(precio_anterior, inflacion_mensual):
    precio_actualizado = precio_anterior * (1 + inflacion_mensual)
    return precio_actualizado

# Ejemplo de uso de la función
precio_anterior = float(input("Ingrese el precio anterior de la planta: "))
inflacion_mensual = float(input("Ingrese el valor de la inflación mensual como decimal (por ejemplo, 0.02 para 2%): "))

nuevo_precio = calcular_precio_actualizado(precio_anterior, inflacion_mensual)
print(f"El nuevo precio actualizado de la planta es: {nuevo_precio:.2f}")