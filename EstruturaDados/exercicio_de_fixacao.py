time_de_dados = []

numero_de_pessoas = int(input('Digite o numero de pessoas do time de dados: '))

for i in range(numero_de_pessoas):
    nome = input('Digite o nome: ')
    cargo = input('Qual a especialidade: ')
    idade = int(input('Digite a idade: '))
    membro = {'nome': nome, 'cargo': cargo, 'idade': idade}
    time_de_dados.append(membro)

for membro in time_de_dados:
    if membro['cargo'] == 'Engenheiro De Dados':
        print(membro['nome'], membro['idade'])