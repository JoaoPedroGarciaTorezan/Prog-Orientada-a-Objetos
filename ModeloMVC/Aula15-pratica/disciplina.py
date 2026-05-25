import tkinter as tk
from tkinter import messagebox

class Disciplina():

    def __init__(self, código, nome):
        self.__código = código
        self.__nome = nome

    @property
    def código(self):
        return self.__código
    
    @property
    def nome(self):
        return self.__nome
    
class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Disciplina")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack()
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelCod = tk.Label(self.frameCod, text='Código: ')
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelCod.pack(side='left')
        self.labelNome.pack(side="left")
    
        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side='left')
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='left')

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side='left')
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side='left')
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side='left')
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraDisciplina():
    def __init__(self, str):
        messagebox.showinfo("Lista de disciplinas ", str)

class CtrlDisciplina():
    def __init__(self):
        self.listaDisciplinas = []

    def insereDisciplina(self):
        self.limiteIns = LimiteInsereDisciplinas(self)

    def mostraDisciplinas(self):
        str = 'Código -- Nome\n'
        for disc in self.listaDisciplinas:
            str += disc.código + ' -- ' + disc.nome + "\n"
        self.limiteLista = LimiteMostraDisciplina(str)

    def enterHandler(self, event):
        cod = self.limiteIns.inputCod.get()
        nome = self.limiteIns.inputNome.get()
        disciplina = Disciplina(cod, nome)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela("Sucesso", 'Disciplina cadastrada!')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCod.delete(0, len(self.limiteIns.inputCod.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
