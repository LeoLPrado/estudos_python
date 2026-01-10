lista_de_supermercado = []

lista_de_supermercado.append('arroz')
lista_de_supermercado.append('feijao')
lista_de_supermercado.append('frutas')
lista_de_supermercado.append('leite')
lista_de_supermercado.append('chocolate')

lista_de_supermercado.remove('frutas')

lista_de_supermercado = []

lista_de_supermercado.append({'item': 'arroz', 'quantidade': '1 kg'})
lista_de_supermercado.append({'item': 'feijao', 'quantidade': '1 kg'})
lista_de_supermercado.append({'item': 'chocolate', 'quantidade': '1 barra'})

for i, coisa in enumerate(lista_de_supermercado):
    print(i, coisa)