import math
x1, y1 = map(float, input().split(' '))
x2, y2 = map(float, input().split(' '))

distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print(f"{distancia:.4f}")