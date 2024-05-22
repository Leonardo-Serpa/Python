from typing import Dict

class Repositorio:

    def select(self, nome) -> Dict:
        return {'nome': nome, 'idade': 32}
    
    def insert(self, nome, idade) -> Dict:
        print(f'Inserindo Dados {nome}, {idade}')
        return {'nome': nome, 'idade': idade}