from produtos import Produto
from carrinho import CarrinhoDeCompras

car = CarrinhoDeCompras()
monitor = Produto('Monitor LG', 1000)

car.adicionar_produto(monitor)

car.finalizar_compra()