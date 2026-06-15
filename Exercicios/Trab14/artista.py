import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import os.path
import pickle

class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__listaAlbuns = []
        self.__listaMusicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def listaAlbuns(self):
        return self.__listaAlbuns
    
    @property
    def listaMusicas(self):
        return self.__listaMusicas
    
    def addAlbum(self, album):
        self.__listaAlbuns.append(album)

    def addMusica(self, musica):
        self.__listaMusicas.append(musica)

    
class limiteInsArtista(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome)
        self.inputNome.pack(side="left")

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

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, str):
        messagebox.showinfo("Artista: ", str)
    
class CtrlArtista:
    def __init__(self):
        self.listaArtistas = []

    def getListaNomes(self):
        listNomes = []
        for art in self.listaArtistas:
            listNomes.append(art.nome)
        return listNomes
    
    def getArtista(self, art):
        for arti in self.listaArtistas:
            if art == arti.nome:
                return arti

    def cadastraArtista(self):
        self.limiteIns = limiteInsArtista(self)
    
    def consultaArtista(self):
        nome = simpledialog.askstring("Consultar Artista", "Informe o nome do Artista: ")
        str = "" 
        if nome:
            for art in self.listaArtistas:
                if art.nome == nome:
                    for alb in art.listaAlbuns:
                        str += "Album: {} \n".format(alb.nome)
                        for mus in art.alb.listaMusicas:
                            str += " - {} \n".format(mus.nome)
            self.limiteCons = LimiteConsultaArtista(str)
            return 
        str = "Artista não encontrado"
        self.limiteCons = LimiteConsultaArtista(str)

    def enterHandler(self, event):
        Nome = self.limiteIns.inputNome.get()
        artista = Artista(Nome)
        self.listaArtistas.append(artista)
        self.limiteIns.mostraJanela("Sucesso", "Artista cadastrado com sucesso!")
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
