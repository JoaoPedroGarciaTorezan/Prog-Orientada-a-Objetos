import tkinter as tk
from tkinter import messagebox
import pizza as piz
import pedidos as ped

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.pizzaMenu = tk.Menu(self.menubar)
        self.pedidoMenu = tk.Menu(self.menubar)    

        self.pizzaMenu.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarPizza)
        self.pizzaMenu.add_command(label="Consultar", \
                    command=self.controle.consultarPizza)
        self.menubar.add_cascade(label="Pizza", \
                    menu=self.pizzaMenu)
        
        self.pedidoMenu.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarPedido)
        self.pedidoMenu.add_command(label="Consultar", \
                    command=self.controle.consultarPedido)
        self.menubar.add_cascade(label="Pedido", \
                    menu=self.pedidoMenu)
        
        self.root.config(menu=self.menubar)


class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlPizza = piz.ctrlPizza()
        self.ctrlPedido = ped.ctrlPedido(self)
        

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Pizzaria Mama Mia")

        self.root.mainloop()
    
    def cadastrarPizza(self):
        self.ctrlPizza.cadastrarPizza()
        
    def consultarPizza(self):
        self.ctrlPizza.consultarPizza()

    def cadastrarPedido(self):
        self.ctrlPedido.cadastrarPedido()

    def consultarPedido(self):
        self.ctrlPedido.consultarPedido()


if __name__ == '__main__':
    c = ControlePrincipal()