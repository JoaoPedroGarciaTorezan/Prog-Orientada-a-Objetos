class Veiculo:
    #construtor
    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    #métodos de instância
    def ligarMotor(self):
        if self.__motorLigado == True:
            print("O motor já está ligado!")
        else:
            self.__motorLigado = True
            print("Motor ligado!")
    def deligarMotor(self):
        if self.__motorLigado == False:
            print("O motor já está desligado!")
        else:
            self.__motorLigado = False
            print("Motor desligado!")
    def mostraAtributos(self, moto, moto1):
        if moto:
            print('Este veículo é uma {} {} {}'.format(self.__marca, self.__cor, moto1.estilo))
        else:
            print('Este veículo é um {} {}'.format(self.__marca, self.__cor))
        if (self.__motorLigado):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')


class Motocicleta(Veiculo):
    #construtor
    def __init__(self, marca, cor, motorLigado, estilo):
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo
    @property
    def estilo(self):
        return self.__estilo


class Carro(Veiculo):
    #construtor
    def __init__(self, marca, cor, motorLigado, portaMalas):
        super().__init__(marca, cor, motorLigado)
        self.__portaMalas = portaMalas

    #método de instância
    def encherPortaMalas(self):
        if self.__portaMalas == True:
            print("Porta-malas cheio!")
        else:
            self.__portaMalas = True
            print("Porta-malas está enchendo!")
    def esvaziarPortaMalas(self):
        if self.__portaMalas == False:
            print("Porta-malas já está vazio!")
        else:
            self.__portaMalas = False
            print("Porta-malas esvaziando!")


carro1 = Carro('Fusca', 'azul', False, False)
moto1 = Motocicleta('Honda', 'vermelha', False, 'esportivo')
moto1.ligarMotor()
moto1.mostraAtributos(True, moto1)
print()
carro1.encherPortaMalas()
carro1.ligarMotor()
carro1.mostraAtributos(False, None)
print()
