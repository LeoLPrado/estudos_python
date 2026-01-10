carrinho_compras = [
    {'nome': 'Chiclete', 'preco': 2.50},
    {'nome': 'Feijao', 'preco': 5.00},
    {'nome': 'Arroz', 'preco': 7.50}
]

print('Deseja iniciar o programa:')
print('0 - Sim   1 - Nao')
opcao_inicial = input()

while opcao_inicial == '0':

    print('1 - Adicionar item ao carrinho, 2 - Remover item pelo nome, 3 - Visualizar itens e total da compra, 0 - Sair')
    opcao = input()
    tamanho_lista = len(carrinho_compras)

    if opcao == '1':
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preco do produto: '))
        carrinho_compras.append({'nome': nome, 'preco': preco})

    elif opcao == '2':
        aux = 0
        print(carrinho_compras)
        produto_removido = input('Digite o nome do produto a ser removido: ')

        for produto in carrinho_compras:
            if produto_removido == produto['nome']:
                carrinho_compras.remove(produto)
            else:
                aux += 1
        
        if aux == tamanho_lista:
            print('Produto nao encontrado')

    elif opcao == '3':
        total = 0

        for produto in carrinho_compras:
            total += produto['preco']
            print(f'Nome do produto: {produto['nome']} R$ {produto['preco']}')
        print(f'Total da compra: {total}')

    elif opcao == '0':
        print('Programa encerrado')
        break

    else:
        print('Opcao invalida')
        print('Deseja continuar o programa:')
        print('0 - Sim   1 - Nao')
        opcao_inicial = input()

print(carrinho_compras)