from abc import ABC, abstractmethod

class Repositorio(ABC):

    @abstractmethod
    def inserir(self, dado):
        pass

    @abstractmethod
    def deletar(self, dado):
        pass