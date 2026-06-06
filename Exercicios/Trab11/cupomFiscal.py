import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog


class CupomFiscal:
    def __init__(self, nro_cupomFiscal, itensCupom):
        self.__nro_cupomFiscal = nro_cupomFiscal
        self.__itensCupom = itensCupom

    @property
    def nro_cupomFiscal(self):
        return self.__nro_cupomFiscal
    
    @property
    def itensCupom(self):
        return self.__itensCupom


class LimiteCadastrarCupomFiscal(tk.Toplevel):
    def __init__(self, controle, listaNomes):

        tk.Toplevel.__init__(self)
        self.geometry('350x250')
        self.title("Cupom Fiscal")
        self.controle = controle

        self.framenro_cupomFiscal = tk.Frame(self)
        self.frameProduto = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framenro_cupomFiscal.pack()
        self.frameProduto.pack()
        self.frameButton.pack()

        self.labenro_cupomFiscal = tk.Label(self.framenro_cupomFiscal,text="Informe o número do cupom fiscal: ")
        self.labenro_cupomFiscal.pack(side='left')
        self.inputnro_cupomFiscal = tk.Entry(self.framenro_cupomFiscal, width=20)
        self.inputnro_cupomFiscal.pack(side="left")

        self.labelProduto = tk.Label(self.frameProduto,text="Escolha os itensCupom a serem adicionados: ")
        self.labelProduto.pack(side="left")
        self.listbox = tk.Listbox(self.frameProduto)
        self.listbox.pack(side="left")
        for nome in listaNomes:
            self.listbox.insert(tk.END, nome)
            
        self.buttonSubmit = tk.Button(self.frameButton ,text="Incluir Item")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.incluirItem)

        self.buttonClear = tk.Button(self.frameButton ,text="Fechar CupomFiscal")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.fechaCupomFiscal)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultarCupomFiscal(tk.Toplevel):
    def __init__(self, str):
        messagebox.showinfo("CupomFiscal ", str)


class ctrlCupomFiscal():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaCupomFiscals = []

    def criarCupomFiscal(self):
        self.listaProdutoTemp = []
        listaNomes = self.ctrlPrincipal.ctrlProduto.getNomeProdutos()
        self.limiteCad = LimiteCadastrarCupomFiscal(self, listaNomes)

    def consultarCupomFiscal(self):
        nroCupom = simpledialog.askstring("Consulta de CupomFiscal", "Informe o número do CupomFiscal: ")
        str1 = ""
        precoParc = 0
        precoTotal = 0
            
             
        if nroCupom:
            for cuFis in self.listaCupomFiscals:
                if nroCupom == cuFis.nro_cupomFiscal:
                    str1 += "Número do CupomFiscal: " + cuFis.nro_cupomFiscal + "\n"
                    for ind, prod in enumerate(cuFis.itensCupom):
                        ind += 1
                        str1 += str(ind) + " " + prod.descricao + ' - R$ ' + "{:.2f}".format(prod.valorUni) + '\n'
                        precoTotal += prod.valorUni
                    str1 += " Total do CupomFiscal: R$ " + "{:.2f}".format(precoTotal) + '\n'
                    self.limiteLista = LimiteConsultarCupomFiscal(str1)
                    return
        str1 = "CupomFiscal não encontrado."
        self.limiteLista = LimiteConsultarCupomFiscal(str1)


    def incluirItem(self, event):
        prodSel = self.limiteCad.listbox.get(tk.ACTIVE)
        item = self.ctrlPrincipal.ctrlProduto.getProduto(prodSel)
        self.listaProdutoTemp.append(item)
        self.limiteCad.mostraJanela('Sucesso', 'Produto incluído com sucesso')

        
    def fechaCupomFiscal(self, event):
        nroCupom = self.limiteCad.inputnro_cupomFiscal.get()
        ped = CupomFiscal(nroCupom, self.listaProdutoTemp)
        self.listaCupomFiscals.append(ped)
        self.limiteCad.mostraJanela('Sucesso', 'CupomFiscal fechado com sucesso')
        self.limiteCad.destroy()

