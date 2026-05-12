class Artista:
    def __init__(self, nome):
        self.__nome = nome 
        # artista agrega albuns e músicas; ambos são listas
        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def albuns(self):
        return self.__albuns

    @property
    def musicas(self):
        return self.__musicas

    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)


class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista # objeto: um album tem um artista
        self.__ano = ano
        #álbum agrega várias músicas
        self.__faixas = []
        artista.addAlbum(self) #chamada de função; agrega álbum ao artista; self- objeto album que acabou de ser criado

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

    #adiciona as músicas ao album; lista faixas
    def addFaixa(self, titulo, artista=None): # musícas de um mesmo artista, não prescisa passar o artista
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__faixas) + 1
        musica = Musica(titulo, artista, self, nroFaixa) #criando música
        self.__faixas.append(musica)


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

    #adiciona as músicas à playlist; 
    def addMusica(self, musica): 
        self.__musicas.append(musica)

if __name__ == "__main__":    
    listaAlbuns = []
    listaplaylists = []
    art1 = Artista('Coldplay')
    album1 = Album('Mylo Xyloto', art1, 2011)
    album1.addFaixa('Paradise')
    album1.addFaixa('Hurts Like Heaven')
    album1.addFaixa('Charlie Brown') 
    listaAlbuns.append(album1)

    album2 = Album('A Head Full of Dreams', art1, 2015)
    album2.addFaixa('A Head Full of Dreams')
    album2.addFaixa('Birds')
    album2.addFaixa('Everglow')
    listaAlbuns.append(album2)

    art2 = Artista('Skank')
    album3 = Album('Siderado', art2, 1998)
    album3.addFaixa('Resposta')
    album3.addFaixa('Saideira')
    album3.addFaixa('Romance Noir')
    listaAlbuns.append(album3)

    # Imprimir o título dos 3 álbuns criados
    print("Títulos dos Álbuns criados: ")
    for album in listaAlbuns:
        print(album.titulo)
    print()

    # Criar e exibir uma playlist com as músicas do album "Mylo Xyloto"
    playlist1 = Playlist("Playlist 1 ")
    print(playlist1.nome)
    for faixa in album1.faixas:
        playlist1.addMusica(faixa)
    listaplaylists.append(playlist1)
    for musica in playlist1.musicas:
        print(musica.titulo)
    print()

    # Criar e exibir uma playlist com todas as músicas do Coldplay 
    playlist2 = Playlist("Playlist 2 ")
    print(playlist2.nome)
    for musica in art1.musicas:
        playlist2.addMusica(musica)
    listaplaylists.append(playlist2)
    for musicas in playlist2.musicas:
        print(musicas.titulo)
    print()

    # Criar e exibiir uma playlist contendo uma música de cada album
    playlist3 = Playlist("Playlist 3 ")
    print(playlist3.nome)
    for album in listaAlbuns:
        playlist3.addMusica(album.faixas[0]) #adiciona a primeira música de cada álbum
    listaplaylists.append(playlist3)
    for musica in playlist3.musicas:
        print(musica.titulo)
    print()

    # Listar o nome de todas as playlists e informar suas musicas
    print("Playlists criadas: ")
    for playlist in listaplaylists:
        print(playlist.nome)
        for musica in playlist.musicas:
            print(" - {}".format(musica.titulo))
    