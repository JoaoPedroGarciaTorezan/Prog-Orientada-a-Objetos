import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
from tkinter import simpledialog

class Produto:
    def __init__(self, codigo, descricao, valorUni, quant=0):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUni = valorUni
        self.__quant = quant

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valorUni(self):
        return self.__valorUni
    
    @property
    def quant(self):
        return self.__quant


class LimiteCadastrarProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Produto")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.framevalorUni = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.framevalorUni.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelDescricao = tk.Label(self.frameDescricao,text="Descrição: ")
        self.labelvalorUni = tk.Label(self.framevalorUni,text="Valor Unitário: ")
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left") 
        self.labelvalorUni.pack(side="left") 

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left")    
        self.inputvalorUni = tk.Entry(self.framevalorUni, width=20)
        self.inputvalorUni.pack(side="left")
       
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultarProduto(tk.Toplevel):
    def __init__(self, str):  
        messagebox.showinfo("Produto: ", str)


class ctrlProduto():
    def __init__(self):
        self.listaProdutos = []

    def getListaProdutos(self):
        return self.listaProdutos
    
    def getProduto(self, Produto):
        prodEsc = None
        for prod in self.listaProdutos:
            if Produto == prod.descricao:
                prodEsc = prod
        return prodEsc
    
    def getNomeProdutos(self):
        listaNomes = []
        for prod in self.listaProdutos:
            listaNomes.append(prod.descricao)
        return listaNomes
    
    def cadastrarProduto(self):
        self.limiteCad = LimiteCadastrarProduto(self)

    def consultarProduto(self):
        codigo = simpledialog.askstring("Consulta Produto", "Informe o código do Produto:")
        str = ""
        if codigo: 
            for prod in self.listaProdutos:
                if codigo == prod.codigo:
                    str += prod.descricao + '- R$ ' + prod.valorUni
                    self.limiteLista = LimiteConsultarProduto(str)
                    return 
        str = "Produto não encontrado. "
        self.limiteLista = LimiteConsultarProduto(str)


    def enterHandler(self, event):
        codigo = self.limiteCad.inputCodigo.get()
        descricao = self.limiteCad.inputDescricao.get()
        valorUni = self.limiteCad.inputvalorUni.get()
        produto = Produto(codigo, descricao, valorUni)
        self.listaProdutos.append(produto)
        self.limiteCad.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteCad.inputCodigo.delete(0, len(self.limiteCad.inputCodigo.get()))
        self.limiteCad.inputDescricao.delete(0, len(self.limiteCad.inputDescricao.get()))
        self.limiteCad.inputvalorUni.delete(0, len(self.limiteCad.inputvalorUni.get()))

