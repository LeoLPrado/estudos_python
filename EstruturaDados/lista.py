animais = ["leao", "gato", "gaivota", "baleia azul"]

# -- todos esses modificam a lista original
#.append(elemento) --> coloca algo no final da lista
#.insert(indice, valor) --> coloca algo na posicao determinada na lista
#.remove() --> remove algo da lista
#.pop(indice) se nao botar indice vai do padrao --> remove itens da lista original
animais.append("vaca")
animais.insert(1, "hipopotamo") #indice, oq vai inserir
animais.remove("leao")
animais.pop() #ou
animais.pop(3) # ambos removem o ultimo elemento

#printa o indice do objeto na lista
print(animais.index("gato"))

#inverte a lista
animais.reverse()

#literalmente copia uma lista
nova_lista = animais.copy()

#bota em ordem alfabetica, modifica a lista original
nova_lista.sort()

print(nova_lista)
print(nova_lista[0]) #acessando o indice de algo na minha lista

#limpa a lista toda
nova_lista.clear()
print(nova_lista)
print(len(nova_lista))

#pedindo o numero de animais que tera na lista para depois preencher a minha lista animais utilizando o metodo .append
numero_de_animais = int(input())

vetor_animais = [] #declarando a minha lista(lista/array)

for i in range(numero_de_animais):
    animal = input()
    vetor_animais.append(animal)

for animal in vetor_animais:
    print(animal)