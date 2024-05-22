class Mae:

    def __init__(self, endereco):
        self.endereco = endereco
        self.sobrenome = 'Silva'

    def comer(self):
        print('Estou comendo')

    def estudar(self):
        print('Estou estudando')

    
class Filha(Mae):

    def __init__(self, endereco):
        super().__init__(endereco)

    def brincar(self, brinquedo):
        print(f'Estou brincando com {brinquedo}!')

clara = Filha('Rua do bolo')
clara.estudar()
clara.brincar('boneca')
print(clara.endereco)