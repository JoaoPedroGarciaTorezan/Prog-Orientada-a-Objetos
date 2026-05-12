from abc import ABC, abstractmethod
import math as mt

class FormaGeo(ABC):
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass 

    @abstractmethod
    def printDados(self):
        pass

class Retangulo(FormaGeo):
    def __init__(self, nome, altura, base):
        super().__init__(nome)
        self.__altura = altura
        self.__base = base

    @property
    def altura(self):
        return self.__altura

    @property
    def base(self):
        return self.__base

    def area(self):
        return self.__altura * self.__base

    def perimetro(self):
        return 2 * (self.__altura + self.__base)

    def printDados(self):
        print(" Nome: {}".format(self.nome))
        print(" Area: {}".format(self.area()))
        print(" Perímetro: {}".format(self.perimetro()))

class Circulo(FormaGeo):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio

    def area(self):
        return 3.14 * self.__raio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.__raio

    def printDados(self):
        print(" Nome: {}".format(self.nome))
        print(" Area: {}".format(self.area()))
        print(" Perímetro: {}".format(self.perimetro()))

class HexagonoRegular(FormaGeo):
    def __init__(self, nome, lado):
        super().__init__(nome)
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado
        
    def area(self):
        return 6 * ((self.__lado ** 2) * mt.sqrt(3) / 4)
        
    def perimetro(self):
        return 6 * self.__lado
        
    def printDados(self):
        print(" Nome: {}".format(self.nome))
        print(" Area: {:.2f}".format(self.area()))
        print(" Perímetro: {}".format(self.perimetro()))

if __name__ == "__main__":
    ret = Retangulo("Quadrado", 5, 5)
    ret.area()
    ret.perimetro()
    ret.printDados()

    print("=========\n")

    circ = Circulo("Círculo 2d", 3)
    circ.area()
    circ.perimetro()
    circ.printDados()

    print("=========\n")

    hex = HexagonoRegular("Hexágono Regular", 4)
    hex.area()
    hex.perimetro()
    hex.printDados()
