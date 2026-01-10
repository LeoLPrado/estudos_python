list_of_dic = [{'nome': 'Leo', 'idade': '19'}]

list_of_dic.append({'nome': 'lara', 'idade': '19'})


# Fazendo usando lista
for i in range(len(list_of_dic)):
    print(f'Nome: {list_of_dic[i]['nome'].capitalize()}, Idade: {list_of_dic[i]['idade']}')

# Fazendo usando dicionario
for pessoa in list_of_dic:
    print(f'Nome: {pessoa['nome'].capitalize()}, Idade: {pessoa['idade']}')