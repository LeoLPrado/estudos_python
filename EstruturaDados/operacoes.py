db = [
    {'nome': 'Leo', 'cargo': 'Engenheiro dados'},
    {'nome': 'Fulano', 'cargo': 'Dev'}
]

def add_user(nome, cargo):
    db.append({'nome': nome, 'cargo': cargo})
    print(f'Usuario {nome} adicionado')

def get_user():
    for u in db:
        print(u)

def update_user(nome, novo_cargo):
    for u in db:
        if u['nome'] == nome:
            u['cargo'] = novo_cargo
            print(f'Usuario {nome} atualizado')

def delete_user(nome):
    aux = len(db)
    i = 0
    for u in db:
        if u['nome'] == nome:
            del db[i]
            print(f'Usuario {nome} deletado')
            break
        i += 1
    if i == aux:
        print(f'Usuario {nome} nao encontrado')

if __name__ == '__main__':
    add_user('Ciclano', 'Gestor')
    get_user()
    update_user('Leo', 'Engenheiro Software')
    get_user()
    delete_user('Maria')