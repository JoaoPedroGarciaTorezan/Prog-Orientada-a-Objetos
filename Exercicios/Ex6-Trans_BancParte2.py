from abc import ABC
from datetime import date

class Transação(ABC):
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data
    
    @property
    def valor(self):
        return self.__valor 
    
    @property
    def data(self):
        return self.__data

class Saque(Transação):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha
    
class Deposito(Transação):
    def __init__(self, valor, data, nomeDep):
        super().__init__(valor, data)
        self.__nomeDep = nomeDep

    @property
    def nomeDep(self):
        return self.__nomeDep

class Transferencia(Transação):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.__tipoTransf = tipoTransf

    @property
    def senha(self):
        return self.__senha
    
    @property
    def tipoTransf(self):
        return self.__tipoTransf

class Conta():
    def __init__(self, nroConta, nome, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self._senha = senha

        self.__transacoes = []

    @property
    def nroConta(self):
        return self.__nroConta
    
    @property
    def nome(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite
    
    @property
    def senha(self):
        return self._senha

    @property
    def transacoes(self):
        return self.__transacoes
    
    def adicionaDeposito(self, valor, data, nomeDep):
        dep = Deposito(valor, data, nomeDep)
        self.transacoes.append(dep)

    def adicionaSaque(self, valor, data, senha):
        saldo = self.calculaSaldo()
        if saldo < valor or senha != self.senha:
            return False
        else: 
            saq = Saque(valor, data, senha)
            self.transacoes.append(saq)
            return True


    def adicionaTransf(self, valor, data, senha, contaFav):
        saldo_c2 = self.calculaSaldo()
        if saldo_c2 < valor or senha != self.senha:
            return False
        else:
            conta1 = Transferencia(valor, data, senha, "D")
            conta2 = Transferencia(valor, data, senha, "C")
            self.transacoes.append(conta1)
            contaFav.transacoes.append(conta2)
            self.calculaSaldo()
            contaFav.calculaSaldo()

            return True


    def calculaSaldo(self):
        saldo = self.limite
        for trans in self.transacoes:
            if isinstance(trans, Deposito):
                saldo += trans.valor
            elif isinstance(trans, Saque):
                saldo -= trans.valor
            elif isinstance(trans, Transferencia):
                if trans.tipoTransf == 'D':
                    saldo -= trans.valor
                    return saldo
                elif trans.tipoTransf == 'C':
                    saldo += trans.valor
                    return saldo
        return saldo
                
    
if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')
    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')

    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 1700