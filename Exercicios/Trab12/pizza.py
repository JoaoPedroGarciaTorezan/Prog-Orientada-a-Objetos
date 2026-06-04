import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
from tkinter import simpledialog

class Pizza:
    def __init__(self, codigo, descricao, preco):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def preco(self):
        return self.__preco


class LimiteCadastrarPizza(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Pizza")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.framePreco.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelDescricao = tk.Label(self.frameDescricao,text="Descrição: ")
        self.labelPreco = tk.Label(self.framePreco,text="Preço: ")
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left") 
        self.labelPreco.pack(side="left") 

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left")    
        self.inputPreco = tk.Entry(self.framePreco, width=20)
        self.inputPreco.pack(side="left")
       
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultarPizza(tk.Toplevel):
    def __init__(self, str):  
        messagebox.showinfo("Pizza: ", str)


class ctrlPizza():
    def __init__(self):
        self.listaPizzas = []

    def getListaPizzas(self):
        return self.listaPizzas
    
    def getPizza(self, pizza):
        pizzEsc = None
        for pizz in self.listaPizzas:
            if pizza == pizz.descricao:
                pizzEsc = pizz
        return pizzEsc
    
    def getNomePizzas(self):
        listaNomes = []
        for pizz in self.listaPizzas:
            listaNomes.append(pizz.descricao)
        return listaNomes
    
    def cadastrarPizza(self):
        self.limiteCad = LimiteCadastrarPizza(self)

    def consultarPizza(self):
        codigo = simpledialog.askstring("Consulta Pizza", "Informe o código da pizza:")
        str = ""
        if codigo: 
            for pizz in self.listaPizzas:
                if codigo == pizz.codigo:
                    str += pizz.codigo + " - " + pizz.descricao + '- R$ ' + pizz.preco
                    self.limiteLista = LimiteConsultarPizza(str)
                    return 
        str = "Pizza não encontrada"
        self.limiteLista = LimiteConsultarPizza(str)


    def enterHandler(self, event):
        codigo = self.limiteCad.inputCodigo.get()
        descricao = self.limiteCad.inputDescricao.get()
        preco = self.limiteCad.inputPreco.get()
        pizza = Pizza(codigo, descricao, preco)
        self.listaPizzas.append(pizza)
        self.limiteCad.mostraJanela('Sucesso', 'Pizza cadastrada com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteCad.inputCodigo.delete(0, len(self.limiteCad.inputCodigo.get()))
        self.limiteCad.inputDescricao.delete(0, len(self.limiteCad.inputDescricao.get()))
        self.limiteCad.inputPreco.delete(0, len(self.limiteCad.inputPreco.get()))

