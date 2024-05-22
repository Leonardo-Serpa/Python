from abs_class import AbstractClass

class Filha(AbstractClass):

    def apresentar_metodo(self):
        print(self.atributo)

    def metodo_abstrato(self):
        print('Implementando método abstrato')

filha = Filha()
filha.apresentar_metodo()
filha.metodo('Estou Aqui')
filha.metodo_abstrato()

#abstractClass = AbstractClass()
abstractClass.metodo('Fazendo algo')