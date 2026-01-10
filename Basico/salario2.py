nome = input()
salario_fixo = float(input())
valor_vendido = float(input())

salario_final = (salario_fixo) + (valor_vendido * 0.15)

print(f"TOTAL = R$ {salario_final:.2f}")