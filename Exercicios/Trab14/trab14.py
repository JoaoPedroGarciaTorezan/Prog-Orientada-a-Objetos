import tkinter as tk
import artista as art
import album as alb

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.ArtistaMenu = tk.Menu(self.menubar)
        self.AlbumMenu = tk.Menu(self.menubar)
        self.PlaylistMenu = tk.Menu(self.menubar)
        
        self.ArtistaMenu.add_command(label="Cadastrar", command=self.controle.cadastraArtista)
        self.ArtistaMenu.add_command(label="Consultar", command=self.controle.consultaArtista)
        self.menubar.add_cascade(label="Artista", menu=self.ArtistaMenu)

        self.AlbumMenu.add_command(label="Cadastrar", command=self.controle.cadastraAlbum)
        self.AlbumMenu.add_command(label="Consultar", command=self.controle.consultaAlbum)
        self.menubar.add_cascade(label="Álbum", menu=self.AlbumMenu)

        self.PlaylistMenu.add_command(label="Cadastrar", command=self.controle.cadastraPlaylist)
        self.PlaylistMenu.add_command(label="Consultar", command=self.controle.consultaPlaylist)
        self.menubar.add_cascade(label="Playlist", menu=self.PlaylistMenu)
               
        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlArtista = art.CtrlArtista()

        self.ctrlAlbum = alb.CtrlAlbum(self)

        #self.ctrlPlaylist = jg.CtrlAlbum(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Spotify Brasileiro")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastraArtista(self):
        self.ctrlArtista.cadastraArtista()
    
    def consultaArtista(self):
        self.ctrlArtista.consultaArtista()

    def cadastraAlbum(self):
        self.ctrlAlbum.cadastraAlbum()

    def consultaAlbum(self):
        self.ctrlAlbum.consultaAlbum()

    def cadastraPlaylist(self):
        self.ctrlPlaylist.cadastraPlaylist()

    def consultaPlaylist(self):
        self.ctrlPlaylist.consultaPlaylist()
    

if __name__ == '__main__':
    c = ControlePrincipal()