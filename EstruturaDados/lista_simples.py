lista_de_empregados = [
    {'nome': 'Ana', 'cargo': 'Pleno'},
    {'nome': 'Joao', 'cargo': 'Junior'},
    {'nome': 'Pedro', 'cargo': 'Senior'}  
]

lista_de_empregados.append({'nome': 'Dri Lopes', 'cargo': 'Garota Noturna'})

def busca_empregado(nome):
    for empregado in lista_de_empregados:
        if nome == empregado['nome']:
            return empregado['cargo']
    return 'Empregado nao encontrado'

nome = input()
print(busca_empregado(nome))
