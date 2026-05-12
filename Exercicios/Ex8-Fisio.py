from abc import ABC, abstractmethod

class Paciente(ABC):
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco

        self.__sessoes = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def sessoes(self):
        return self.__sessoes
    
    def addSessao(self, sessao):
        self.sessoes.append(sessao)

    @abstractmethod
    def geraFichaPaciente(self, mes=None):
        pass

    @abstractmethod
    def calculaValorDevido(self, mes):
        pass

class Particular(Paciente):
    def __init__(self, nome, endereco, cpf):
        super().__init__(nome, endereco)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf
    
    def geraFichaPaciente(self, mes=None):
        print("Nome: {}".format(self.nome))
        print("Endereco: {}".format(self.endereco))
        print("CPF: {}".format(self.cpf))
        print("Sessoes realizadas: ")
        print("Dia  - Tipo")
        for ses in self.sessoes:
            if mes:
                if ses.mes == mes:
                    print("{}/{} - {}".format(ses.dia,ses.mes,ses.tipo.nome))
            else:
                print("{}/{} - {}".format(ses.dia,ses.mes,ses.tipo.nome))
                

    def calculaValorDevido(self, mes):
        valor = 0
        for ses in self.sessoes:
            if ses.mes == mes:
                if ses.tipo.nome == 'Respiratória':
                    valor += ses.tipo.preco
                elif ses.tipo.nome == 'Pilates':
                    valor += ses.tipo.preco
                elif ses.tipo.nome == 'Ortopédica':
                    valor += ses.tipo.preco
        return valor


class Convenio(Paciente):
    def __init__(self, nome, endereco, nomeConv, nroCartao):
        super().__init__(nome, endereco)
        self.__nomeConv = nomeConv
        self.__nroCartao = nroCartao

    @property
    def nomeConv(self):
        return self.__nomeConv
    
    @property
    def nroCartao(self):
        return self.__nroCartao
    
    def geraFichaPaciente(self, mes=None):
        print("Nome: {}".format(self.nome))
        print("Endereco: {}".format(self.endereco))
        print("Convênio: {}".format(self.nomeConv))
        print("Nro Cartão: {}".format(self.__nroCartao))
        print("Sessoes realizadas: ")
        print("Dia  - Tipo")
        for ses in self.sessoes:
            if mes:
                if ses.mes == mes:
                    print("{}/{} - {}".format(ses.dia,ses.mes,ses.tipo.nome))
            else:
                print("{}/{} - {}".format(ses.dia,ses.mes,ses.tipo.nome))

    def calculaValorDevido(self, mes):
        valor = 0
        for ses in self.sessoes:
            if ses.mes == mes:
                if ses.tipo.nome == 'Respiratória':
                    valor += ses.tipo.preco
                elif ses.tipo.nome == 'Pilates':
                    valor += ses.tipo.preco
                elif ses.tipo.nome == 'Ortopédica':
                    valor += ses.tipo.preco
        return valor * 0.6

class Sessao():
    def __init__(self, dia, mes, tipo):
        self.__dia = dia
        self.__mes = mes
        self.__tipo = tipo

    @property
    def dia(self):
        return self.__dia
    
    @property
    def mes(self):
        return self.__mes
    
    @property
    def tipo(self):
        return self.__tipo
    
class TipoSessao():
    def __init__(self, nome, duracao, preco):
        self.__nome = nome
        self.__duracao = duracao
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome
    
    @property
    def duracao(self):
        return self.__duracao
    
    @property
    def preco(self):
        return self.__preco
    

if __name__=="__main__":
    listaPac = []
    orto = TipoSessao('Ortopédica', 30, 50)
    resp = TipoSessao('Respiratória', 40, 60)
    pil = TipoSessao('Pilates', 50, 70)
    pac1 = Convenio('Pedro', 'Av BPS, 1303', 'Unimed', 123456)
    pac1.addSessao(Sessao(10, 9, resp))
    pac1.addSessao(Sessao(12, 9, resp))
    pac1.addSessao(Sessao(18, 9, pil))
    pac1.addSessao(Sessao(5, 10, resp))
    listaPac.append(pac1)
    pac2 = Particular('Maria', 'Av Cesario Alvin, 55', 654321)
    pac2.addSessao(Sessao(11, 9, orto))
    pac2.addSessao(Sessao(15, 9, orto))
    pac2.addSessao(Sessao(23, 9, pil))
    pac2.addSessao(Sessao(12, 10, orto))
    listaPac.append(pac2)
    pac1.geraFichaPaciente(10)
    print()
    pac2.geraFichaPaciente()
    print()
    faturamento = 0
    for paciente in listaPac:
        faturamento += paciente.calculaValorDevido(9)
    print('Faturamento do mês 9: {}'.format(faturamento))