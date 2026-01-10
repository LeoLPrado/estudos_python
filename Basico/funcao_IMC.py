def calc_IMC(altura, peso):
    imc = peso / (altura * altura)
    return  imc

altura = float(input())
peso = float(input())

print(calc_IMC(altura, peso))