valor = int(input())

nota100 = int(valor / 100)
print(f"{nota100} nota(s) de R$ 100,00")

resto = valor - (nota100 * 100)

nota50 = int(resto / 50)
print(f"{nota50} nota(s) de R$ 50,00")

resto2 = resto - (nota50 * 50)

nota20 = int(resto2 / 20)
print(f"{nota20} nota(s) de R$ 20,00")

resto3 = resto2 - (nota20 * 20)

nota10 = int(resto3 / 10)
print(f"{nota10} nota(s) de R$ 10,00")

resto4 = resto3 - (nota10 * 10)

nota5 = int(resto4 / 5)
print(f"{nota5} nota(s) de R$ 5,00")

resto5 = resto4 - (nota5 * 5)

nota2 = int(resto5 / 2)
print(f"{nota2} nota(s) de R$ 2,00")

resto6 = resto5 - (nota2 * 2)

nota1 = int(resto6 / 1)
print(f"{nota1} nota(s) de R$ 1,00")