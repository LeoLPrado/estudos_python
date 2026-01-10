horas = int(input())
velocidade_media = int(input())

distancia = velocidade_media * horas
# 12km/L

consumo = distancia / 12
print (f"{consumo:.3f}")