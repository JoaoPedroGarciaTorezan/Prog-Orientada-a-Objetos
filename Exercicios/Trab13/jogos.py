import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco, avaliacoes):
        self.codigo = codigo
        self.titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco
        self.__avaliacoes = avaliacoes

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        if not valor or valor <= 0:
            if not valor:
                raise ValueError("Código não pode ser vazio.")
            else:
                raise ValueError("Código não pode ser negativo.")
        self.__codigo = valor

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, valor):
        self.titulo = ['*', '@', '#', '$', '%', '&']
        if not valor or valor in self.titulo:
            if not valor:
                raise ValueError("Título não pode ser vazio.")
            else:
                raise ValueError("Título não pode conter caracteres especiais.")
        self.__titulo = valor

    @property
    def console(self):
        return self.__console
    
    @console.setter
    def console(self, valor):
        self.consoles = ["PlayStation", "Xbox", "Switch", "PC"]
        if not valor or valor not in self.consoles:
            if not valor:
                raise ValueError("Console não pode ser vazio.")
            else:
                raise ValueError("Console inválido: {}".format(valor))
        self.__console = valor

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, valor):
        self.generos = ["Ação", "Aventura", "RPG", "Esporte", "Estratégia", "Simulação"]
        if not valor or valor not in self.generos:
            if not valor:
                raise ValueError("Gênero não pode ser vazio.")
            else:
                raise ValueError("Gênero inválido: {}".format(valor))
        self.__genero = valor
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0 or valor > 500:
            if valor < 0:
                raise ValueError("Preço não pode ser negativo.")
            else:
                raise ValueError("Preço não pode ser maior que 500.")
        self.__preco = valor

    @property
    def avaliacoes(self):
        return self.__avaliacoes
    
    def getJogo(self):
        return "Título: " + str(self.titulo)\
        + "\nCódigo: " + str(self.codigo)\
        + "\nConsole: " + str(self.console)\
        + "\nGênero: " + str(self.genero)\
        + "\nPreço: " + str(self.preco)
    
class LimiteInsereJogo(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Jogo")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelTitulo = tk.Label(self.frameTitulo,text="Título: ")
        self.labelConsole = tk.Label(self.frameConsole, text="Console: ")
        self.labelGenero = tk.Label(self.frameGenero, text="Gênero: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preço: ")
        self.labelCodigo.pack(side="left")
        self.labelTitulo.pack(side="left")
        self.labelConsole.pack(side="left")
        self.labelGenero.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo)
        self.inputTitulo = tk.Entry(self.frameTitulo)
        self.inputConsole = tk.Entry(self.frameConsole)
        self.inputGenero = tk.Entry(self.frameGenero)
        self.inputPreco = tk.Entry(self.framePreco)
        self.inputCodigo.pack(side="left")
        self.inputTitulo.pack(side="left")
        self.inputConsole.pack(side="left")
        self.inputGenero.pack(side="left")
        self.inputPreco.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    
class CtrlJogo:
    def __init__(self, controle):
        self.controle = controle
        self.jogos = []

    def cadastraJogo(self):
        self.limiteInsere = LimiteInsereJogo(self)

    def enterHandler(self, event):
        codigo = self.limiteInsere.inputCodigo.get()
        titulo = self.limiteInsere.inputTitulo.get()
        console = self.limiteInsere.inputConsole.get()
        genero = self.limiteInsere.inputGenero.get()
        preco = float(self.limiteInsere.inputPreco.get())

        try:
            jogo = Jogo(codigo, titulo, console, genero, preco, [])
            self.jogos.append(jogo)
            self.limiteInsere.mostraJanela("Sucesso", "Jogo cadastrado com sucesso!")
            self.clearHandler(event)
        except ValueError as error:
            self.limiteInsere.mostraJanela("Erro", str(error))

    def clearHandler(self, event):
        self.limiteInsere.inputCodigo.delete(0, len(self.limiteInsere.inputCodigo.get()))
        self.limiteInsere.inputTitulo.delete(0, len(self.limiteInsere.inputTitulo.get()))
        self.limiteInsere.inputConsole.delete(0, len(self.limiteInsere.inputConsole.get()))
        self.limiteInsere.inputGenero.delete(0, len(self.limiteInsere.inputGenero.get()))
        self.limiteInsere.inputPreco.delete(0, len(self.limiteInsere.inputPreco.get()))