from .interface import Repositorio

class MongoRepositorio(Repositorio):

    def inserir(self, dado):
        print(f'Inserindo {dado} no banco MongoDB')

    def deletar(self, dado):
        print(f'Deletando {dado} do banco MongoDB')