from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

        self.__pontoMensalFunc = []

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc
    
    def adicionaPonto(self, mes, ano, faltas, atrasos):
        ponto = PontoFunc(mes, ano, faltas, atrasos)
        self.pontoMensalFunc.append(ponto)


    def lancaFaltas(self, mes, ano, faltas):
        for pont in self.pontoMensalFunc:
            if mes == pont.mes and ano == pont.ano:
                pont.lancaFaltas(faltas)

    def lancaAtrasos(self, mes, ano, atrasos):
        for pont in self.pontoMensalFunc:
            if mes == pont.mes and ano == pont.ano:
                pont.lancaAtrasos(atrasos)

    def imprimeFolha(self, mes, ano):
        salario = self.calculaSalario(mes, ano)
        bonus = self.calculaBonus(mes, ano)
        print("Código: {}".format(self.codigo))
        print("Nome: {}".format(self.nome))
        print("Salário líquido: {}".format(salario))
        print("Bonus: {:.2f}".format(bonus))

    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass

class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas

    @property
    def titulacao(self):
        return self.__titulacao
    
    @property
    def salarioHora(self):
        return self.__salarioHora
    
    @property
    def nroAulas(self):
        return self.__nroAulas
    
    def calculaSalario(self, mes, ano):
        for pont in self.pontoMensalFunc:
            if mes == pont.mes and ano == pont.ano:
                return self.salarioHora * self.nroAulas - self.salarioHora * pont.nroFaltas

    def calculaBonus(self, mes, ano):
        for pont in self.pontoMensalFunc:
            if mes == pont.mes and ano == pont.ano:
                return self.calculaSalario(mes,ano) * (0.1 - 0.01*pont.nroAtrasos)


class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    @property
    def funcao(self):
        return self.__funcao
    
    @property
    def salarioMensal(self):
        return self.__salarioMensal
    
    
    def calculaSalario(self, mes, ano):
        for pont in self.pontoMensalFunc:
            if mes == pont.mes and ano == pont.ano:
                return self.salarioMensal - (self.salarioMensal/30) * pont.nroFaltas


    def calculaBonus(self, mes, ano):
        for pont in self.pontoMensalFunc:
            if mes == pont.mes and ano == pont.ano:
                return self.calculaSalario(mes,ano) * (0.08 - 0.01*pont.nroAtrasos)


class PontoFunc():
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

    @property
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def nroFaltas(self):
        return self.__nroFaltas
    
    @property
    def nroAtrasos(self):
        return self.__nroAtrasos
    
    def lancaFaltas(self, nroFaltas):
        self.__nroFaltas = nroFaltas

    def lancaAtrasos(self, nroAtrasos):
        self.__nroAtrasos = nroAtrasos


if  __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()