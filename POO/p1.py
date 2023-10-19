class Produto:
    def __init__(self, name, quantity, value):
        self.name = str(name)
        self.quantity = int(quantity)
        self.value = float(value)
    def calcular_total(self):
        return float(self.quantity * self.value)


class Carrinho:
    produtos = []
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        produto.quantity -= 1
    def calcular_total_carrinho(self):
        total = float()
        for produto in self.produtos:
            total += produto.value
        return total

produto1 = Produto('Arroz', 20, 20.00)
produto2 = Produto('Feijão', 30, 15.00)
produto3 = Produto('Batata', 60, 2.00)

carrinho = Carrinho

carrinho.adicionar_produto(carrinho, produto1)
carrinho.adicionar_produto(carrinho, produto2)
carrinho.adicionar_produto(carrinho, produto3)
carrinho.adicionar_produto(carrinho, produto2)


print(carrinho.calcular_total_carrinho(carrinho))