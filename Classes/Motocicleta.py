class Motocicleta:
    #construtor
    def __init__(self, marca, cor, motorligado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorligado
    #método de instância
    def ligarMotor(self):
        if self.__motorLigado == True:
            print("Motor ligado!")
        else:
            self.__motorLigado
            print("O motor já esta ligado!")
    def mostraAtributos(self):
        print('Esta motocicleta é uma {} {}'.format(self.__marca, self.__cor))
        if (self.__motorLigado):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')


moto1 = Motocicleta('Honda', 'vermelha', False)
moto1.mostraAtributos()
print()
moto1.ligarMotor()
print()
moto1.mostraAtributos()
print()
moto1.ligarMotor()