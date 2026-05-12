from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria

    @property
    def nome(self):
        return self.__nome
    @property
    def matricula(self):
        return self.__matricula
    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

    @abstractmethod
    def calculaSalario(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salario):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter     #setter - muda o valor do atributo
    def salario(self, salario):
        self.__salario = salario

    def calculaSalario(self):
        return self.__salario

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    @property
    def salarioHora(self):
        return self.__salarioHora

    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora 

    def calculaSalario(self):
        return self.__salarioHora * self.cargaHoraria

if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)
    prof1.salario = 6000   # usando o método setter
    prof2.salarioHora = 85
    profs = [prof1, prof2, prof3]
    for prof in profs:
        print ('Nome: {} - Salário: {}'.format(prof.nome, prof.calculaSalario()))

