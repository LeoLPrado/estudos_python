numeros_de_votos = int(input())
gostou = 0
nao_gostou = 0
vetor_opiniao = []

for i in range(numeros_de_votos):
    voto = int(input())
    vetor_opiniao.append(voto)

for i in range(numeros_de_votos):
    if vetor_opiniao[i] == 1:
        gostou += 1
    if vetor_opiniao[i] == -1:
        nao_gostou += 1

if gostou > nao_gostou:
    print ("A maioria gostou")

elif nao_gostou > gostou:
    print ("A maioria nao gostou")

else:
    print ("Deu empate")