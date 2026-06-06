import tkinter as tk
from tkinter import messagebox
import produto as prod
import cupomFiscal as cf

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.produtoMenu = tk.Menu(self.menubar)
        self.CupomFiscalMenu = tk.Menu(self.menubar)    

        self.produtoMenu.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarProduto)
        self.produtoMenu.add_command(label="Consultar", \
                    command=self.controle.consultarProduto)
        self.menubar.add_cascade(label="Produto", \
                    menu=self.produtoMenu)
        
        self.CupomFiscalMenu.add_command(label="Cadastrar", \
                    command=self.controle.criarCupomFiscal)
        self.CupomFiscalMenu.add_command(label="Consultar", \
                    command=self.controle.consultarCupomFiscal)
        self.menubar.add_cascade(label="Cupom Fiscal", \
                    menu=self.CupomFiscalMenu)
        
        self.root.config(menu=self.menubar)


class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = prod.ctrlProduto()
        self.ctrlCupomFiscal = cf.ctrlCupomFiscal(self)
        

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Loja de Conivência")

        self.root.mainloop()
    
    def cadastrarProduto(self):
        self.ctrlProduto.cadastrarProduto()
        
    def consultarProduto(self):
        self.ctrlProduto.consultarProduto()

    def criarCupomFiscal(self):
        self.ctrlCupomFiscal.criarCupomFiscal()

    def consultarCupomFiscal(self):
        self.ctrlCupomFiscal.consultarCupomFiscal()


if __name__ == '__main__':
    c = ControlePrincipal()