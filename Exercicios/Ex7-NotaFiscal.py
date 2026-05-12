from datetime import date
from abc import ABC, abstractmethod

class Venda(ABC):
    def __init__(self, nroNF, dtEmissao):
        self.__nroNF = nroNF
        self.__dtEmissao = dtEmissao

        self.__itens = []

    @property
    def nroNF(self):
        return self.__nroNF
    
    @property
    def dtEmissao(self):
        return self.__dtEmissao
    
    @property
    def itens(self):
        return self.__itens
    
    def adicionaItem(self, pCodProd, pQuant, pPrecoUnit):
        item = Item_Venda(pCodProd, pQuant, pPrecoUnit)
        self.itens.append(item)

    def calculaTotalVendido(self):
        total = 0
        for item in self.itens:
            total += item.quant * item.precoUnit
        return total

    @abstractmethod
    def geraNF(self):
        pass

    @abstractmethod
    def calculaImposto(self):
        pass

class VendaPF(Venda):
    def __init__(self, nroNF, dtEmissao, cpf, nome):
        super().__init__(nroNF, dtEmissao)
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    def geraNF(self):
        return str(self.nroNF)

    def calculaImposto(self):
        total = self.calculaTotalVendido()
        return total * 0.09


class VendaPJ(Venda):
    def __init__(self, nroNF, dtEmissao, cnpj, nomeFantasia):
        super().__init__(nroNF, dtEmissao)
        self.__cnpj = cnpj
        self.__nomeFantasia = nomeFantasia

    @property
    def cnpj(self):
        return self.__cnpj
    
    @property
    def nomeFantasia(self):
        return self.__nomeFantasia
    
    def geraNF(self):
        return str(self.nroNF)

    def calculaImposto(self):
        total = self.calculaTotalVendido()
        return total * 0.06

class Item_Venda():
    def __init__(self, codProd, quant, precoUnit):
        self.__codProf = codProd
        self.__quant = quant
        self.__precoUnit = precoUnit

    @property
    def codProf(self):
        return self.__codProf
    
    @property
    def quant(self):
        return self.__quant
    
    @property
    def precoUnit(self):
        return self.__precoUnit
    

if __name__ == "__main__":
    totalFaturado = 0
    totalImposto = 0
    vendas = []
    vendapf = VendaPF(1000, date.today(), '123456789', 'Joao')
    vendapf.adicionaItem(100, 10, 10)
    vendapf.adicionaItem(100, 10, 20)
    vendapf.adicionaItem(100, 10, 30)
    vendas.append(vendapf)
    vendapj = VendaPJ(1001, date.today(), '987654321', 'Silva Ltda')
    vendapj.adicionaItem(200, 100, 10)
    vendapj.adicionaItem(201, 100, 20)
    vendas.append(vendapj)
    for venda in vendas:
        totalFaturado += venda.calculaTotalVendido()
        totalImposto += venda.calculaImposto()
    print('Total faturado: {}'.format(totalFaturado))
    print('Total pago em impostos: {}'.format(totalImposto))