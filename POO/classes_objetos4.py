class ContaBancaria:
    # Atributo de classe (compartilhado por todas as instancias)
    banco = 'Banco Python'

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo
    
    # Getter (metodo para extrair uma informacao privada/encapsulada)
    @property # decorator
    def saldo(self):
        return self._saldo
    
    # Metodo para depositar
    # Setter
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Deposito de R${valor} realizado')
        
        else:
            print('Valor invalido para deposito')
    
    # Metodo de classe
    @classmethod
    def info_banco(cls):
        print(f'Informacoes do {cls.banco}')


# Usando a classe:
conta1 = ContaBancaria('Joao', 1000)
conta2 = ContaBancaria('Maria')

# Demonstrando atributo de classe:
print('Banco: ', ContaBancaria.banco)
print('Saldo =', conta1.saldo)