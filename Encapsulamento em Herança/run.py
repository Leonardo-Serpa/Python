class DatabaseConn:

    def __init__(self):
        self.__database = 'Postgres'
        self._conn = '//connection_string'
        self.user = 'Leo'


    def get_database(self):
        print(f'conectando ao banco {self.__database}')

    def _testing_connection(self):
        print('Connection is OK!')


class Repository(DatabaseConn):
    
    def __init__(self):
        super().__init__()

    def select(self):
        self._testing_connection()
        print(f'connecting to {self._conn}')
        print('SELECT * FROM table')
        print(self.user)


repo = Repository()
repo.select()



    