import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Pedido:
    def __init__(self, nro_pedido, quant, pizza):
        self.__nro_pedido = nro_pedido
        self.__quant = quant
        self.__pizza = pizza


    @property
    def nro_pedido(self):
        return self.__nro_pedido
    
    @property
    def quant(self):
        return self.__quant
    
    @property
    def pizza(self):
        return self.__pizza


class LimiteCadastrarPedido(tk.Toplevel):
    def __init__(self, controle, listaNomes):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Pedidos")
        self.controle = controle

        self.frameNro_pedido = tk.Frame(self)
        self.framequant = tk.Frame(self)
        self.framePizza = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro_pedido.pack()
        self.framequant.pack()
        self.framePizza.pack()
        self.frameButton.pack()

        self.labeNro_pedido = tk.Label(self.frameNro_pedido,text="Informe o número do pedido: ")
        self.labeNro_pedido.pack(side='left')
        self.inputNro_pedido = tk.Entry(self.frameNro_pedido, width=20)
        self.inputNro_pedido.pack(side="left")

        self.labelPizza = tk.Label(self.framePizza,text="Escolha o sabor da pizza: ")
        self.labelPizza.pack(side="left")
        self.escolhaCombo1 = tk.StringVar()
        self.combobox1 = ttk.Combobox(self.framePizza, width = 15 , textvariable = self.escolhaCombo1)
        self.combobox1.pack(side="left")
        self.combobox1['values'] = listaNomes

        self.labelPizza = tk.Label(self.framePizza,text="Escolha o sabor da pizza: ")
        self.labelPizza.pack(side="left")
        self.escolhaCombo2 = tk.StringVar()
        self.combobox2 = ttk.Combobox(self.framePizza, width = 15 , textvariable = self.escolhaCombo2)
        self.combobox2.pack(side="left")
        self.combobox2['values'] = listaNomes

        self.labelQuant = tk.Label(self.framequant,text="Informe a quantidade: ")
        self.labelQuant.pack(side='left')
        self.inputQuant = tk.Entry(self.framequant, width=20)
        self.inputQuant.pack(side="left")
       
        self.buttonSubmit = tk.Button(self.frameButton ,text="Incluir Pizza")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.inserePizza)

        self.buttonClear = tk.Button(self.frameButton ,text="Fechar Pedido")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.fechaPedido)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultarPedido(tk.Toplevel):
    def __init__(self, str):
        messagebox.showinfo(str)


class ctrlPedido():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPedidos = []

    def cadastrarPedido(self):
        self.listaPizzaTemp = []
        listaNomes = self.ctrlPrincipal.ctrlPizza.getNomePizzas()
        self.limiteCad = LimiteCadastrarPedido(self, listaNomes)

    def consultarPedido(self):
        nroPed = self.limiteCad.inputNro_pedido.get()
        possui_atributo = any(hasattr(ped, nroPed) for ped in self.listaPedidos)  
        if possui_atributo == False:
            str = "Não foi possivel encontrar este número de pedido." 
            self.limiteLista = LimiteConsultarPedido(str)
        else: 
            for pizz in self.listaPizzas:
                str += pizz.codigo + " - " + pizz.quant + '- R$ ' + pizz.preco
            self.limiteLista = LimiteConsultarPedido(str)


    def inserePizza(self, event):
        pizzaSel1 = self.limiteCad.escolhaCombo1
        pizzaSel2 = self.limiteCad.escolhaCombo2
        pizz1 = self.ctrlPrincipal.ctrlPizza.getPizza(pizzaSel1)
        pizz2 = self.ctrlPrincipal.ctrlPizza.getPizza(pizzaSel2)
        self.listaPizzaTemp.append(pizz1)
        self.listaPizzaTemp.append(pizz2)

        

    def fechaPedido(self, event):
        nroPed = self.limiteCad.inputNro_pedido.get()
        pizzaSel1 = self.limiteCad.escolhaCombo1
        pizzaSel2 = self.limiteCad.escolhaCombo2
        pizz1 = self.ctrlPrincipal.ctrlPizza.getPizza(pizzaSel1)
        pizz2 = self.ctrlPrincipal.ctrlPizza.getPizza(pizzaSel2)
        quant = self.limiteCad.inputQuant.get()
        ped = Pedido(nroPed, pizz1, pizz2, quant)
        self.listaPedidos.append(ped)
        self.limiteCad.mostraJanela('Sucesso', 'Pedido fechado com sucesso')
        self.limiteCad.destroy()

