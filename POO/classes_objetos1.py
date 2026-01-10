# Definindo uma classe simples

class Pessoa:

    # Metodo construtor: dunder function
    def __init__(self, nome, idade):
        
        # Atributos da classe (self, nome, idade)
        # self = um objeto comum a nossa classe | um objeto acessivel por todos os metodos

        self.nome = nome
        self.idade = idade

    # Metodo (funcao de uma classe) para apresentacao
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
    
    def diga_seu_nome(self):
        print(f'Claro, meu nome é: {self.nome}')

# Criando objetos
pessoa1 = Pessoa('Joao', 25)
pessoa2 = Pessoa('Maria', 30)


# Chamando metodos:

pessoa1.apresentar()
pessoa1.diga_seu_nome()
pessoa2.apresentar()
pessoa2.diga_seu_nome()

# Acessando atributos:

print(f'Nome da primeira pessoa: {pessoa1.nome}')
print(f'Nome da primeira pessoa: {pessoa2.nome}')