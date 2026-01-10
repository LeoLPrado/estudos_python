import random

lista_imagens = ['💎', '🍬', '7']

print ("🎰 Bem-vindo ao Caça-Níquel Python! 🎰")
print("\nPressione ENTER para girar os rolos...")
acao = input()

def girar_rolos():
    rolo = random.choice(lista_imagens)
    return rolo

def jogar():
    print("Girando...")
    if acao == "":
        resultado = [girar_rolos(), girar_rolos(), girar_rolos()]
        print(f'\n| {resultado[0]} | {resultado[1]} | {resultado[2]} |')

    if resultado[0] == resultado[1] == resultado[2]:
        print("\n PARABENS !! VOCE GANHOU O PREMIO!")
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        print("\nVoce chegou perto.")
    else:
        print("\n Nao foi dessa vez. Tente Novamente.")

while acao == "":
    jogar()
    print("\nPressione ENTER para girar novamente ou digite 'q' para sair.")
    acao = input().lower()

    if acao == 'q':
        print('\nObrigado por jogar! Até a próxima.')