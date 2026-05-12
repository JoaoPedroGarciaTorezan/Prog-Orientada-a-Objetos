class Animal:
    #construtor
    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca
    
    @property #propriedade
    def nome(self):
        return self.__nome
    
    @property #propriedade
    def raca(self):
        return self.__raca
    
    def fazerCarinho(self):
        print('O animal {} está recebendo carinho'.format(self.__nome))

class Gato(Animal):
    #Construtor
    def __init__(self, nome, raca):
        #super é usado para acessar a superclasse
        super().__init__(nome, raca)

    
    def miar(self):
        print("Miau Miau")

class Cao(Animal): #PS: Cão é uma classe sem atributo
    #Construtor
    def __init__(self, nome, raca):
        #super é usado para acessar a superclasse
        super().__init__(nome, raca)

    def latir(self):
        print("Au Au")

gato = Gato('Mingau', 'Persa')
print(gato.nome)
print(gato.raca)
gato.miar()
gato.fazerCarinho()
print()
cao = Cao('Caju', 'Labrador')
print(cao.nome)
print(cao.raca) 
cao.latir()
cao.fazerCarinho()
print()