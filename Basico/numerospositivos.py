valores_positivos = 0
soma_num = 0

for i in range (6):
    num = float(input())

    if num >= 0:
        valores_positivos += 1

    soma_num += num

media = soma_num / 6

print(f"{valores_positivos} valores psotivos")
print(media)