# Inicializar contadores para cada candidato
candidato1 = 0
candidato2 = 0
candidato3 = 0

# Simular el voto de los 200 electores
for _ in range(200):
    voto = int(input("Ingrese el número del candidato por el que desea votar (1, 2 o 3): "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("Voto inválido, por favor ingrese un número válido de candidato.")

# Determinar al ganador por mayoría simple
if candidato1 > candidato2 and candidato1 > candidato3:
    print("El ganador es el candidato 1.")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print("El ganador es el candidato 2.")
elif candidato3 > candidato1 and candidato3 > candidato2:
    print("El ganador es el candidato 3.")
else:
    print("Hubo un empate en la votación.")
