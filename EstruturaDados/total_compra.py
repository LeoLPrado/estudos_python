lista_de_itens = [
    {'Trident': 6.00},
    {'Bala': 5.30},
    {'Picole': 3.20},
    {'Pipoca': 2.50}
]

item_comprado = input()
quantidade_comprada = int(input())

def calcula_total(item_comprado, quantia):
    for item in lista_de_itens:
        if item_comprado in item:
            preco = item[item_comprado]
            valor = preco * quantia
            return valor
    return 'Produto nao encontrado'

print(calcula_total(item_comprado, quantidade_comprada))