# Inicializar el inventario con 1000 vacunas disponibles
inventario = 1000

# Simular el funcionamiento diario
def funcionamiento_diario(entregas):
    global inventario
    inventario -= entregas
    if inventario < 200:
        print("¡Alerta! El inventario de vacunas ha bajado de 200 unidades.")

# Ejemplo de funcionamiento diario con entregas
entregas_del_dia = int(input("Ingrese la cantidad de vacunas entregadas hoy: "))
funcionamiento_diario(entregas_del_dia)