# Criando base/pai
class Animal:
    def __init__(self, nome):
        # Atributo protegido self._
        self._nome = nome # atributo protegido/ privado
    
    def fazer_som(self):
        print('Som generico de animal')


# Classe derivada/filho (heranca)
class Cachorro(Animal): # Super classe
    def __init__(self, nome, raca):
        # Chamando construtor da classe pai
        super().__init__(nome)
        self.raca = raca
    
    # Sobrescrevendo metodo/ o primeiro polimorfismo
    def fazer_som(self):
        print('Au!, Au!')
    
    def abanar_rabo(self):
        print(f'{self._nome} esta abanando o rabo!')


# Criando objetos:
animal_generico = Animal('Bicho')
rex = Cachorro('Rex', 'Pastor Alemao')

# Verificando tipos:
print('\nVerificacao de tipos: ')
print(isinstance(animal_generico, Cachorro)) # false
print('O que é o nosso bicho?', type(animal_generico))
print('Rex é um cachorro?', isinstance(rex, Cachorro))
print('rex é um animal?', isinstance(rex, Animal)) # Cachorro deriva de animal

# Demonstrando polimorfismo:
print('Sons de animais:')
animal_generico.fazer_som()
rex.fazer_som()

# Metodo especifico de Cachorro:
rex.abanar_rabo()
# animal_generico.abanar_rabo() --> erro, pois o animal_generico nao tem o metodo de abanar o rabo