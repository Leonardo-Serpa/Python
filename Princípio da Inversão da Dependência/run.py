from typing import Type
from db.interface import Repositorio
from db.mysql_repositorio import MySqlRepositorio
from db.mongo_repositorio import MongoRepositorio

class Usuario:

    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.repositorio = repositorio

    def armazenar_dados(self, dado: any) -> None:
        self.repositorio.inserir(dado)

    def remover_dados(self, dado: any) -> None:
        self.repositorio.deletar(dado)

#usuario = Usuario(MySqlRepositorio())

usuario = Usuario(MySqlRepositorio())
usuario.armazenar_dados(23)

usuario = Usuario(MongoRepositorio())
usuario.armazenar_dados(23)