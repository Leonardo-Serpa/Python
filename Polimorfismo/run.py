from models import Insersor, Repositorio

class RepositorioFake(Repositorio):

    def __init__(self) -> None:
        super().__init__()

    def select(self, name: int) -> None:
        return None

repo = RepositorioFake()
insersor = Insersor(repo)

data = insersor.inserir_dado('Leo', 24)
print(data)