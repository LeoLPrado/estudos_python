numero_de_usuarios = int(input())
maior = -99999999999
menor = 99999999999

vetor_contatos = []

# preenchendo meu vetor
for i in range(numero_de_usuarios):
    num = int(input())
    vetor_contatos.append(num)

#analisando o maior e o menor numero de contatos do meu vetor
for i in range(numero_de_usuarios):
    if vetor_contatos[i] > maior:
        maior = vetor_contatos[i]
    
    if vetor_contatos[i] < menor:
        menor = vetor_contatos[i]

print(f"Maior numero de contatos: {maior}")
print(f"Menor numero de contatos: {menor}")