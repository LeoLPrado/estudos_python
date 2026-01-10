vendedores = [
    {'nome': 'Ana', 'cargo': 'Pleno'},
    {'nome': 'Joao', 'cargo': 'Junior'},
    {'nome': 'Pedro', 'cargo': 'Senior'}
]

multiplicadores = {
    'Junior': 1.0,
    'Pleno': 1.1,
    'Senior': 1.25
}


def buscar_vendedor(nome_vendedor):
    for vendedor in vendedores:
        if vendedor['nome'] == nome_vendedor:
            return vendedor
        


def calc_comissao(nome, total_vendas):
    vendedor = buscar_vendedor(nome)

    if not vendedor:
        print('Vendedor nao encontrado')

    cargo = vendedor['cargo']
    multiplicador = multiplicadores[cargo]

    if total_vendas <= 999:
        comissao = total_vendas * multiplicador
    
    elif total_vendas > 999 and total_vendas <= 2000:
        comissao = (total_vendas * 0.05) + (total_vendas * multiplicador)
    
    elif total_vendas > 2000:
        comissao = (total_vendas * 0.1) + (total_vendas * multiplicador)
    
    return comissao


    
nome_vendedor = input()
total_vendas = int(input())
resultado = calc_comissao(nome_vendedor, total_vendas)
print(resultado)