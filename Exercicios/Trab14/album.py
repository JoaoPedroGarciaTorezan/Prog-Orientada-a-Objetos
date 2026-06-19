import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import os.path
import pickle

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = []
        artista.addAlbum(self)

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def ano(self):
        return self.__ano

    @property
    def faixas(self):
        return self.__faixas
    
    @faixas.setter
    def faixas(self, faixas):
        self.__faixas = faixas.copy()
    
    def addAlbum(self, album):
        self.__listaAlbuns.append(album)

class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

        artista.addMusica(self) # relacionamento extra

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista

    @property
    def album(self):
        return self.__album

    @property
    def nroFaixa(self):
        return self.__nroFaixa

    
class LimiteCadastraAlbum(tk.Toplevel):
    def __init__(self, controle, listaNomes):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Album")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameFaixa = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameFaixa.pack()
        self.frameButton.pack()
      
        self.labelTitulo = tk.Label(self.frameTitulo, text="Titulo: ")
        self.labelTitulo.pack(side="left")
        self.inputTitulo = tk.Entry(self.frameTitulo)
        self.inputTitulo.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista,text="Insira o artista do álbum: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomes

        self.labelAno = tk.Label(self.frameAno, text="Ano: ")
        self.labelAno.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno)
        self.inputAno.pack(side="left")

        self.labelFaixa = tk.Label(self.frameFaixa, text="Faixa: ")
        self.labelFaixa.pack(side="left")
        self.inputFaixa = tk.Entry(self.frameFaixa)
        self.inputFaixa.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Insere Faixa")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.InsereFaixa)

        self.buttonCriaAlbum = tk.Button(self.frameButton ,text="Cria Álbum")      
        self.buttonCriaAlbum.pack(side="left")
        self.buttonCriaAlbum.bind("<Button>", controle.criaAlbum)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, str):
        messagebox.showinfo("Album: ", str)
    
class CtrlAlbum:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlbums = []

    def cadastraAlbum(self):
        self.faixaTemp = []
        nomesArtists = self.ctrlPrincipal.ctrlArtista.getListaNomes()
        self.limiteCad = LimiteCadastraAlbum(self, nomesArtists)

    def InsereFaixa(self, event):
        titulo = self.limiteCad.inputFaixa.get()
        artNome = self.limiteCad.escolhaCombo.get()
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(artNome)
        nroFaixa = len(self.faixaTemp) +1
        musica = Musica(titulo, artista, self, nroFaixa)
        self.faixaTemp.append(musica)
        self.limiteCad.mostraJanela("Sucesso", "Faixa inserida com sucesso!")
        self.limiteCad.inputFaixa.delete(0, tk.END)
    
    def consultaAlbum(self):
        Titulo = simpledialog.askstring("Consultar Album", "Informe o Titulo do Album: ")
        str = "" 
        if Titulo:
            for alb in self.listaAlbums:
                if alb.titulo == Titulo:
                    str += "Album: {} \n".format(alb.titulo)
                    for mus in alb.faixas:
                        str += " - {} \n".format(mus.titulo)
        if not str:
            str = "Album não encontrado"
        self.limiteCons = LimiteConsultaAlbum(str)

    def criaAlbum(self, event):
        Titulo = self.limiteCad.inputTitulo.get()
        ano = int(self.limiteCad.inputAno.get())
        artNome = self.limiteCad.escolhaCombo.get()
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(artNome)
        self.faixas = self.fechaHandler(event)
        album = Album(Titulo, artista, ano)
        album.faixas = self.faixaTemp.copy()
        self.listaAlbums.append(album)
        self.limiteCad.mostraJanela("Sucesso", "Album cadastrado com sucesso!")
        self.clearHandler(event)
        self.fechaHandler(event)
 
    def clearHandler(self, event):
        self.limiteCad.inputTitulo.delete(0, tk.END)
        self.limiteCad.inputAno.delete(0, tk.END)

    def fechaHandler(self, event):
        self.limiteCad.destroy()
