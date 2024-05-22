from .interface import Repositorio 

class MySqlRepositorio(Repositorio):

    def inserir(self, dado):
        print(f'Inserindo {dado} no banco MySql')

    def deletar(self, dado):
        print(f'Deletando {dado} do banco MySql')