lista_geral = []
lista_limpeza = []
lista_higiene = []
lista_alimentos = []

class Item():
    def __init__(self, nome, preco, quantidade, categoria):
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = int(quantidade)
        self.categoria = categoria.lower()
        if categoria.lower() == 'limpeza':
            lista_limpeza.append(self)
            lista_geral.append(self)
        elif categoria.lower() == 'higiene':
            lista_higiene.append(self)
            lista_geral.append(self)
        elif categoria.lower() == 'alimento':
            lista_alimentos.append(self)
            lista_geral.append(self)
        else:
            Exception('categoria inválida')
        print(f'\nitem adicionado\n {self.nome}, {self.preco:.2f}, {self.quantidade}x, {self.categoria}')
        
    def mostrar_lista_limpeza(self):
        print('Lista Limpeza')
        for item in lista_limpeza:
            print(f'\n {item.nome}, {item.preco:.2f}, {item.quantidade}, {item.categoria}')
        total = 0.0
        for preco in lista_limpeza:
            preco += total
        print(f'Valor total lista Limpeza: R$ {total:.2f}')     

    def mostrar_lista_higiene(self):
        print('Lista Higiene')
        for item in lista_higiene:
            print(f'\n {item.nome}, {item.preco:.2f}, {item.quantidade}, {item.categoria}')
        total = 0.0
        for preco in lista_higiene:
            preco += total
        print(f'Valor total lista Higiene: R$ {total:.2f}')       

    def mostrar_lista_alimentos(self):
        print('Lista Alimentos')
        for item in lista_alimentos:
            print(f'\n {item.nome}, {item.preco:.2f}, {item.quantidade}, {item.categoria}')
        total = 0.0
        for preco in lista_alimentos:
            preco += total
        print(f'Valor total Lista Aimentos: R$ {total:.2f}')     

    def mostrar_lista_geral(self):
        print('Lista Geral')
        for item in lista_geral:
            print(f'\n {item.nome}, {item.preco:.2f}, {item.quantidade}, {item.categoria}')
        total = 0.0
        for preco in lista_geral:
            preco += total
        print(f'Valor total Geral: R$ {total:.2f}')

item1 = Item('Água Sanitária', 12, 5, 'limpeza')
item2 = Item('Pasta de Dente', 14, 3, 'Higiene')
item3 = Item('Café Moído', 15.00, 8, 'alimento')
