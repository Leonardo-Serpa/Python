from typing import Type

class Conexao:
    
    def conectar(self):
        print('Conectando ao banco de dados...')
        
    def desconectar(self):
        print('Desconectando do banco de dados...')


class MysqlRepo(Conexao):

    def __init__(self) -> None:
        super().__init__()

    def select(self):
        self.conectar()
        print('Fazendo um SELECT * FROM table')


class CasoDeUso:
    
    def buscar(self, db_repo: Type[MysqlRepo]):
        db_repo.select()


db_repo_Sql = MysqlRepo()
db_repo_Sql.select()
    
        