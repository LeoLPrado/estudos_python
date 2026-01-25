menu = {
    'Pizza': 75,
    'Hamburguer': 40,
    'Pao de queijo': 4.50,
    'Macarrao': 28
}

class CustomerOrder:
    def __init__(self, nome: str):
        self.nome = nome
        self.pedidos = []

    def add_order(self, item: str):
        if item in menu:
            self.pedidos.append(item)
            print(f'{item} foi adicionado a lista de pedidos.')
        else:
            print(f'{item} nao esta no menu.')
    
    def remove_order(self, item: str):
        if item in self.pedidos:
            self.pedidos.remove(item)
            print(f'{item} foi removido da lista de pedidos')
        else:
            print(f'{item} nao foi pedido por voce ainda.')
    
    def get_total(self) -> float:
        total = 0
        for pedido in self.pedidos:
            total += menu[pedido]
        return print(f'Total = R$ {total}')
    
    def list_order(self):
        if not self.pedidos:
            print('Lista de pedidos vazia, faca um novo pedido.')
        else:
            print(f'Pedidos de {self.nome}:')
            for pedido in self.pedidos:
                print(f'- {pedido}: R$ {menu[pedido]}')

customer = CustomerOrder('Leo')

customer.add_order('Pizza')
customer.get_total()
customer.list_order()
customer.add_order('Pao de queijo')
customer.list_order()
customer.get_total()
