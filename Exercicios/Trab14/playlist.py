import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk

class Playlist:
    def __init__(self, nome):
        self.__nome = nome

        self.__musicas = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas
    

class LimiteCadastraPlaylist(tk.Toplevel):
    def __init__(self, controle, listaNomes):

        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title("Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameArtista.pack()
        self.frameMusica.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome, text="Nome da playlist: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome)
        self.inputNome.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista,text="Selecione o artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width = 15 , values=listaNomes, textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox.bind("<<ComboboxSelected>>", self.controle.exibeMusicas)

        self.labelMusica = tk.Label(self.frameMusica,text="Escolha as músicas: ")
        self.labelMusica.pack(side="left") 
        self.listbox = tk.Listbox(self.frameMusica)
        self.listbox.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Insere Musica")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.InsereMusica)

        self.buttonCriaPlaylist = tk.Button(self.frameButton ,text="Cria Álbum")      
        self.buttonCriaPlaylist.pack(side="left")
        self.buttonCriaPlaylist.bind("<Button>", controle.criaPlaylist)

    def mostraJanela(self, Nome, msg):
        messagebox.showinfo(Nome, msg)

class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, str):
        messagebox.showinfo("Playlist: ", str)


class CtrlPlaylist:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPlaylists = []

    def cadastraPlaylist(self):
        self.MusicaTemp = []
        nomesArtists = self.ctrlPrincipal.ctrlArtista.getListaNomes()
        nomesArtists.append("Vários Artistas")
        self.limiteCad = LimiteCadastraPlaylist(self, nomesArtists)

    def InsereMusica(self, event):
        artSel = self.limiteCad.combobox.get()
        musSel = self.limiteCad.listbox.get()
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(artSel)
        for mus in artista.listaMusicas:
            if mus.nome == musSel:
                    self.MusicaTemp.append(mus)
        self.limiteCad.mostraJanela("Sucesso", "Música inserida com sucesso!")
        self.limiteCad.listbox.delete(tk.ACTIVE)

    
    def consultaPlaylist(self):
        nome = simpledialog.askstring("Consultar Playlist", "Informe o nome da Playlist: ")
        str = "" 
        if nome:
            for play in self.listaPlaylists:
                if play.nome == nome:
                    str += "Playlist: {} \n".format(play.nome)
                    for mus in play.musicas:
                        str += " - {} \n".format(mus.titulo)
            self.limiteCons = LimiteConsultaPlaylist(str)
            return 
        str = "Playlist não encontrada"
        self.limiteCons = LimiteConsultaPlaylist(str)

    def criaPlaylist(self, event):
        nome = self.limiteCad.inputNome.get()
        playlist = Playlist(nome)
        playlist.musicas = self.MusicaTemp.copy()
        self.listaPlaylists.append(playlist)
        self.limiteCad.mostraJanela("Sucesso", "Album cadastrado com sucesso!")
        self.clearHandler(event)
        self.fechaHandler(event)

    def clearHandler(self, event):
        self.limiteCad.inputTitulo.delete(0, tk.END)
        self.limiteCad.inputAno.delete(0, tk.END)

    def fechaHandler(self, event):
        self.limiteCad.destroy()

    def exibeMusicas(self, event):
        artSel = self.limiteCad.combobox.get()
        art = self.ctrlPrincipal.ctrlArtista.getArtista(artSel)
        for mus in art.listaMusicas:
            self.limiteCad.listbox.insert(1.0, mus.nome + "\n\n")
        self.limiteCad.listbox.config(state="disabled")

