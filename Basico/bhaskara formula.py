import math
a, b, c = map(float, input().split(' '))

delta = (b * b) - (4 * a * c)

if delta >= 0 and a != 0:
    R1 = ((-b) + (math.sqrt(delta))) / (2 * a)
    R2 = ((-b) - (math.sqrt(delta))) / (2 * a)
    print (f"R1 = {R1:.5f}")
    print (f"R2 = {R2:.5f}")

else:
    print("Impossivel calcular")