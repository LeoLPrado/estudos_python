# Conceitos de classes e objetos.
# Criacao de Classes.
# Atribuicao e metodos.
# Construtores e inicializacao de objetos.

# Classes --> sao um modelo para criar objetos que vao compartilhar das mesma regras. Classes costumam ser representacoes digitais de coisas
# que existem no mundo real.

#Objeto --> Uma instancia(versao) especifica de uma classe.

-------------------------------------------------------------------------------------------------------------------------------------------

# EXistem 3 pilares funcamentais quando se fala de POO:

# 1 - Heranca: pense numa arvore genealogica onde o filho herda caracteristicas dos pais(altura, cor do olho)
    # Classe veiculo (acelerar, freiar, buzinar) ---> depois podemos criar outras classes mais espcificas como 'carro' e 'moto' que herdam
    # essas caracteristicas  basicas de veiculos, logo nao precisamos reescrever o codigo das carac. basicas para cada tipo de veiculo

# 2 - Polimorfismo: um mesmo comando(metodo) funcionando de formas diferentes dependendo do contexto, imagine um metodo 'fazerSom()' em diferentes bicho
    # Na classe "Cachorro":  fazerSom() produz 'Au Au'
    # Na classe "Gato": fazerSom() produz 'Miau Miau'
    # Na classe "Vaca": fazerSom() produz 'Muuuu'

# 3 - Encapsulamento: imagine uma TV moderna. Voce precisa so apertar alguns botoes no controle para usa-la (ligar, desligar, mudar canal),
    # mas nao precisa entender toda a complexidade eletronica que existe dentro dela.
    # O encapsulamento é como 'esconder' toda a complexidade interna e mostrar somente os "botoes" necessarios para usar algo.
    # Na pratica é como se fosse criar uma "Classe TV" onde voce só expoe os metodos necessarios ( ligar(), desligar()) e esconde toda a complexidade interna