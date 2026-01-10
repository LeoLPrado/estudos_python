#Crie uma classe 'Carro' com atributos como modelo , ano , metodos para:
#Ligar o carro
#Desligar o carro
#Acelerar
#Velocidade atual
#Estado do carro(Ligado ou desligado)

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self._velocidade = 0
    
    def estado_atual(self):
        if self.ligado == True:
            print('O carro esta ligado, pronto para partir')
        else:
            print('O carro esta desligado, dê partida para ligar')

    def ligar_carro(self):
        if self.ligado == False:
            self.ligado = True
        else:
            print('Voce nao pode ligar um carro que esta ja esta ligado')
    
    def desligar_carro(self):
        if self.ligado == True:
            self.ligado = False
        else:
            print('Voce nao pode desligar um carro que esta ja esta desligado')
    
    def acelerar(self, nova_velocidade):
        if self.ligado == True and nova_velocidade > 0:
            self._velocidade += nova_velocidade
        else:
            print('Antes de acelerar ligue o carro')
    
    def velocidade_atual(self):
        return self._velocidade

carro1 = Carro('Ferrari Puro Sangue', 2025)
carro2 = Carro('Ford Fiesta', 2015)