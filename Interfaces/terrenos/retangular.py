from interfaces.formas import FormasInterface

class TerrenoRetangular(FormasInterface):

    def __init__(self, comprimento, largura) -> int:
        self.comprimento = comprimento
        self.largura = largura

    def get_perimetro(self) -> int:
        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return perimetro
    
    def get_area(self) -> int:
        area = self.comprimento * self.largura
        return area
        
    