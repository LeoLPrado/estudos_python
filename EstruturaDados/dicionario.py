biblioteca = {
    'autor': 'Jorge Amado',
    'titulo': 'Capitaes da Areia',
    'ano': '1947'
}

biblioteca['nota'] = 9.4 #adiciona nova chave e valor
biblioteca['ano'] = '1937' #troca o valor de uma determinada chave

del biblioteca['nota'] #remove uma chave-valor
print(biblioteca.keys())
print(biblioteca.values())