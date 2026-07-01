import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import os.path
import pickle

"""Sumário: 
Entry - campo de entrada de dados
Combobox - lista suspensa para seleção de opções
Listbox - lista de itens para seleção (estatico e variavel)
Text - área de texto para exibir informações 
Botão - aciona ações
Setter -> validar informações antes de atribuir valores a atributos privados
Salvamento de dados - persistência de informações em arquivos usando pickle
Askstring - caixa de diálogo para entrada de texto
set() - remove duplicatas de uma lista
"""


class CupomFiscal:
    def __init__(self, nro_cupomFiscal, itensCupom):
        self.__nro_cupomFiscal = nro_cupomFiscal
        self.__itensCupom = itensCupom
        self.setter = setter #(sem underline)

    @property
    def nro_cupomFiscal(self):
        return self.__nro_cupomFiscal
    
    @property
    def itensCupom(self):
        return self.__itensCupom

    @tipo.setter #Validação do tipo do vinho
    def tipo(self, valor):
        self.tipos = ["Branco", "Tinto", "Rose", "Espumante"]
        if not valor in self.tipos:
            raise ValueError("Tipo inválido: {}".format(valor))
        else:
            self.__tipo = valor
    


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

        # entrada normal
        self.labenro_cupomFiscal = tk.Label(self.framenro_cupomFiscal,text="Informe o número do cupom fiscal: ")
        self.labenro_cupomFiscal.pack(side='left')
        self.inputnro_cupomFiscal = tk.Entry(self.framenro_cupomFiscal, width=20)
        self.inputnro_cupomFiscal.pack(side="left")

        #list box com valores fixos
        self.labelProduto = tk.Label(self.frameProduto,text="Escolha os itensCupom a serem adicionados: ")
        self.labelProduto.pack(side="left")
        self.listbox = tk.Listbox(self.frameProduto)
        self.listbox.pack(side="left")
        for nome in listaNomes:
            self.listbox.insert(tk.END, nome)

        # Comobox
        self.labelEspecialidade = tk.Label(self.frameEspecialidade,text="Escolha a especialidade: ")
        self.labelEspecialidade.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameEspecialidade, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = valores
        self.combobox.bind("<<ComboboxSelected>>", self.controle.exibeEspecialidade)

        # Text - pode não ter botão
        self.textConsultas = tk.Text(self.frameConsultas, height=20, width=40)
        self.textConsultas.pack(side='left')
        self.textConsultas.config(state=tk.DISABLED)
            
        self.buttonSubmit = tk.Button(self.frameButton ,text="Incluir Item")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.incluirItem)

        self.buttonClear = tk.Button(self.frameButton ,text="Fechar CupomFiscal")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.fechaCupomFiscal)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultarCupomFiscal(tk.Toplevel):
    # mostra os dados na janela
    def __init__(self, str):
        messagebox.showinfo("CupomFiscal ", str)


class ctrlCupomFiscal():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if not os.path.isfile("cupomFiscals.pickle"):
            self.listaCupomFiscals = []
        else:
            try:
                with open("cupomFiscals.pickle", "rb") as f:
                    self.listaCupomFiscals = pickle.load(f)
            except EOFError:
                self.listaCupomFiscals = []

    def salvarCupomFiscals(self):
        if len(self.listaCupomFiscals) != 0:
            with open("cupomFiscals.pickle", "wb") as f:
                pickle.dump(self.listaCupomFiscals, f)

    def criarCupomFiscal(self):
        self.listaProdutoTemp = []
        listaNomes = self.ctrlPrincipal.ctrlProduto.getNomeProdutos()
        self.limiteCad = LimiteCadastrarCupomFiscal(self, listaNomes)

    def consultarCupomFiscal(self):
        nroCupom = simpledialog.askstring("Consulta de CupomFiscal", "Informe o número do CupomFiscal: ")
        str1 = ""
        precoParcial = 0
        precoTotal = 0     
        if nroCupom:
            for cuFis in self.listaCupomFiscals:
                if nroCupom == cuFis.nro_cupomFiscal:
                    str1 += "Número do CupomFiscal: " + cuFis.nro_cupomFiscal + "\n"
                    for prod in set(cuFis.itensCupom): #set -> tira itens repetidos
                        precoParcial = float(prod.valorUni)*float(prod.quant)
                        str1 += str(prod.quant) + " - " + prod.descricao + ' - R$ ' + "{:.2f}".format(precoParcial) + '\n'
                        precoTotal += precoParcial
                    str1 += " Total do CupomFiscal: R$ " + "{:.2f}".format(precoTotal) + '\n'
                    self.limiteLista = LimiteConsultarCupomFiscal(str1)
                    return
        str1 = "CupomFiscal não encontrado."
        self.limiteLista = LimiteConsultarCupomFiscal(str1)


    def incluirItem(self, event):
        prodSel = self.limiteCad.listbox.get(tk.ACTIVE)
        item = self.ctrlPrincipal.ctrlProduto.getProduto(prodSel)
        item.quant += 1
        self.listaProdutoTemp.append(item)
        self.limiteCad.mostraJanela('Sucesso', 'Produto incluído com sucesso')

        
    def fechaCupomFiscal(self, event):
        nroCupom = self.limiteCad.inputnro_cupomFiscal.get()
        ped = CupomFiscal(nroCupom, self.listaProdutoTemp)
        self.listaCupomFiscals.append(ped)
        self.limiteCad.mostraJanela('Sucesso', 'CupomFiscal fechado com sucesso')
        self.limiteCad.destroy()

    def exibeConsultas(self, event):
        medSel = self.limiteCons.combobox.get()
        self.limiteCons.textConsultas.config(state='normal')
        self.limiteCons.textConsultas.delete(1.0, tk.END)
        for med in self.listaMedicos:
            if med.nome == medSel:
                self.limiteCons.textConsultas.insert(1.0, med.infoMedico() + "\n\n")
        self.limiteCons.textConsultas.config(state='disabled') # se eu posso interagir ou n com o texto

    #ListBox para inserir
    def exibeEspecialidade(self, event):
        espcSel = self.limiteIns.combobox.get()
        listaMedicos = self.ctrlPrincipal.ctrlMedico.getListaMedicos()
        self.limiteIns.listbox.delete(0, tk.END)
        for med in listaMedicos:
            if med.especialidade == espcSel:
                self.limiteIns.listbox.insert(tk.END, med.nome)

