from abc import ABC, abstractmethod
from datetime import date

class Conta(ABC):
    def __init__(self, nroConta, nome, saldo):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__saldo = saldo

        self.__listaTrans = []

    @property
    def nroConta(self):
        return self.__nroConta
    
    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def listaTrans(self):
        return self.__listaTrans
    
    @abstractmethod
    def imprimirExt(self):
        pass
    
    def deposito(self, valor, descricao):
        trans = Transação(valor, descricao)
        self.listaTrans.append(trans)
        self.__saldo += valor

    def saque(self, valor,descricao):
        if self.saldo >= valor:
            self.saldo += valor
            trans = Transação(valor, descricao)
            self.listaTrans.append(trans)
        else: 
            print(" Não a saldo suficiente para o saque. \n")

    def imprimeTransação(self):
        print(" Transações: ")
        for i in self.__listaTrans:
            print(" Valor: {} - Descr: {} ".format(i.valor, i.descricao))

class Corrente(Conta):
    def __init__(self, nroConta, nome, saldo, taxa_mensal):
        super().__init__(nroConta, nome, saldo)
        self.__taxa_mensal = taxa_mensal

    @property
    def taxa_mensal(self):
        return self.__taxa_mensal

    def imprimirExt(self):
        print("Extrato conta Corrente: \n")
        print(" Número da conta: {}".format(self.nroConta))
        print(" Nome: {}".format(self.nome))
        print(" Saldo: {:.2f}".format(self.saldo))
        self.imprimeTransação()

class Limite(Conta):
    def __init__(self, nroConta, nome, saldo, valor_limite):
        super().__init__(nroConta, nome, saldo)
        self.__valor_limite = valor_limite

    @property
    def valor_limite(self):
        return self.__valor_limite
    
    def saque(self, valor, descricao):
        if self.saldo + valor >= self.valor_limite:
            self.saldo += valor
            trans = Transação(valor, descricao)
            self.listaTrans.append(trans)
        else:
            print(" Não é possível fazer saque. Ultrapassou o limite estabelecido. \n")

    def imprimirExt(self):
        print("Extrato conta Corrente com Limite: \n")
        print(" Número da conta: {}".format(self.nroConta))
        print(" Nome: {}".format(self.nome))
        print(" Saldo: {:.2f}".format(self.saldo))
        print(" Valor do limite: {}".format(self.valor_limite))
        self.imprimeTransação()

class Poupanca(Conta):
    def __init__(self, nroConta, nome, saldo, dia_Aniv):
        super().__init__(nroConta, nome, saldo)
        self.__dia_Aniv = dia_Aniv

    @property
    def dia_Aniv(self):
        return self.__dia_Aniv

    def imprimirExt(self):
        print("Extrato conta Poupança: \n")
        print(" Número da conta: {}".format(self.nroConta))
        print(" Nome: {}".format(self.nome))
        print(" Saldo: {:.2f}".format(self.saldo))
        print(" Dia do aniversário: {}".format(self.dia_Aniv))
        self.imprimeTransação()

class Transação():
    def __init__(self, valor, descricao):
        self.__valor = valor
        self.__descricao = descricao

    @property
    def data(self):
        return self.__data 
    
    @property
    def valor(self):
        return self.__valor 
    
    @property
    def descricao(self):
        return self.__descricao
    
if __name__ == "__main__":
    list_contas = []
    conta_corr = Corrente(12345, "Gabriel", 0, 20.00)
    conta_lim = Limite(54321, "Pedro", 0, -120.00)
    conta_poup = Poupanca(676767, "Victor", 0, date(2026, 4, 12))
    conta_corr.deposito(1000.00, "Crédito")
    conta_lim.saque(-30.00, "Débito")
    conta_poup.saque(-70.00, "Débito")
    conta_poup.deposito(1200.00, "Crédito")
    conta_poup.saque(-500.00, "Débito")
    list_contas.append(conta_corr)
    list_contas.append(conta_lim)
    list_contas.append(conta_poup)
    for lista in list_contas:
        lista.imprimirExt()
        print()
        
