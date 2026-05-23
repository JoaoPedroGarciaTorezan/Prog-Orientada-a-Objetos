import tkinter as tk
from tkinter import messagebox, simpledialog

class Model():
    def __init__(self, nome, codigo):
        self.__nome = nome
        self.__codigo = codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo

    
class View():
    def __init__(self, master, controller):
        self.__controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()

        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2, text="Código: ")

        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")

        self.buttonSubmit = tk.Button(self.janela, text="Salva")
        self.buttonSubmit.pack(side='left')
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)

        self.buttonLista = tk.Button(self.janela, text="Lista")
        self.buttonLista.pack(side='left')
        self.buttonLista.bind("<Button>", controller.listaHandler)

        self.button1 = tk.Button(self.janela, text="Botão 1")
        self.button1.pack(side='left')
        self.button1.bind("<Button>", lambda e: controller.contagem(1))

        self.button2 = tk.Button(self.janela, text="Botão 2")
        self.button2.pack(side='left')
        self.button2.bind("<Button>", lambda e: controller.contagem(2))

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo,mensagem)
    
class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x100')
        self.listaPessoas = []
        self.contagem_1 = 0
        self.contagem_2 = 0

        self.view = View(self.root, self)

        self.root.title("Exemplo")

        self.root.mainloop()

    def salvaHandler(self, event):
        nome = self.view.inputText1.get()
        codigo = self.view.inputText2.get()
        cliente = Model(nome, codigo)
        self.listaPessoas.append(cliente)
        self.view.mostraJanela('Sucesso', 'Pessoa cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))

    def contagem(self, botton):
        if botton == 1:
            self.contagem_1 += 1
            self.view.mostraJanela("Número de apertos botão 1: ", str(self.contagem_1))
        elif botton == 2:
            self.contagem_2 += 1
            self.view.mostraJanela("Número de apertos botão 2: ", str(self.contagem_2))
        
    def listaHandler(self, event):
        if len(self.listaPessoas) == 0:
            self.view.mostraJanela('Nenhuma pessoa cadastrada', 'Não há pessoas cadastradas para exibir')
        else:
            self.msg = "Pessoas cadastradas:\n"
            for p in self.listaPessoas:
                self.msg += p.nome + " - " + p.codigo + "\n"
            self.view.mostraJanela('Lista de Pessoas', self.msg)  

if __name__ == "__main__":
    c = Controller()