from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, valorPorHora, horasTrabalhadas):
        super().__init__(nome, telefone)
        self.__valorPorHora = valorPorHora
        self.__horasTrabalhadas = horasTrabalhadas

    @property
    def valorPorHora(self):
        return self.__valorPorHora
    
    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas

    def getSalario(self):
        return self.__valorPorHora * self.__horasTrabalhadas
    
class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, valorPorDia, diasTrabalhados):
        super().__init__(nome, telefone)
        self.__valorPorDia = valorPorDia
        self.__diasTrabalhados = diasTrabalhados

    @property
    def valorPorDia(self):
        return self.__valorPorDia
    
    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados

    def getSalario(self):
        return self.__valorPorDia * self.__diasTrabalhados
    
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    @property
    def valorMensal(self):
        return self.__valorMensal
    
    def getSalario(self):
        return self.__valorMensal
    
if __name__ == "__main__":
    listaEmpregadas = []
    #cria as empregadas
    horista = Horista("Maria", "1198765", 12.0, 160)
    diarista = Diarista("Joana", "1112345", 65.0, 20)
    mensalista = Mensalista("Ana", "1123242", 1200.0)

    #adiciona as empregadas à lista
    listaEmpregadas.append(horista)
    listaEmpregadas.append(diarista)
    listaEmpregadas.append(mensalista)

    #achando qual tem menor salário
    menor = listaEmpregadas[0].getSalario()
    empr_menor = listaEmpregadas[0]
    for emp in listaEmpregadas:
        print(f"Empregada: {emp.nome} - Salário: {emp.getSalario()}")
        if emp.getSalario() < menor:
            menor = emp.getSalario()
            empr_menor = emp
    print()
    print(f"Empregada com menor salário: \nNome: {empr_menor.nome} \nTelefone: {empr_menor.telefone} \nSalário: {menor}")
