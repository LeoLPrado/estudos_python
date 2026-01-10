numero_de_casos = int(input())

for i in range (numero_de_casos):
    num = int(input())

    if num >= 0 and num % 2 == 0:
        print("POSITIVO E PAR")
    
    elif num >= 0 and num % 2 != 0:
        print("POSITIVO E IMPAR")
    
    elif num < 0 and num % 2 == 0:
        print("NEGATIVO E PAR")
    
    else:
        print("NEGATIVO E IMPAR")