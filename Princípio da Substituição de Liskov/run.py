class PessoaA:

    def se_apresentar(self):
        print('Olá, sou a PessoaA')


class PessoaB(PessoaA):
    
    def __init__(self) -> None:
        super().__init__()

    def se_apresentar(self):
        print('Olá, estou alterando o método')

pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()