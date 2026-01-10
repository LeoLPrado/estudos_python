vetor_numeros = []
tamanho_lista = 0

def encontrar(vetor, X, N):
    aux = 0
    for num in vetor:
        if num == X:
           return print ('Numero encontrado')
        else:
            aux += 1
    if aux == tamanho_lista:
        return print('Numero nao encontrado')

num = int(input())
while num != 0:
    vetor_numeros.append(num)
    tamanho_lista += 1
    num = int(input())

X = int(input())
encontrar(vetor_numeros, X, tamanho_lista)