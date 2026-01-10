# Classe co metodos especiais
class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    # Metodo especial para representacao em string ( dunder function) que modifica o print
    def __str__(self):
        return f'{self.titulo} por {self.autor} ({self.ano})'
    
    # Metodo para comparacao
    def __eq__(self, outro): #objeto1 == outro
        return (self.titulo == outro.titulo and
                self.autor == outro.autor and
                self.ano == outro.ano)

# Criando objetos livro:
livro1 = livro('Dom Quixote', 'Miguel de Cervantes', 1605)
livro2 = livro('Dom Quixote', 'Miguel de Cervantes', 1605)
livro3 = livro('O Pequeno Principe', 'Antoine de Saint-Exupéry', 1943)

#Usando os metodos especiais:
print('Representacao do livro:', livro1)
print('Livros sao iguais?', livro1 == livro2)
print('Livros diferentes sao iguais?', livro1 == livro3)