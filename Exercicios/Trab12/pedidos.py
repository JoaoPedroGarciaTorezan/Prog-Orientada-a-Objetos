import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import pizza as piz


class Pedido:
    def __init__(self, nro_pedido, quant, pizzas, precoTotal):
        self.__nro_pedido = nro_pedido
        self.__quant = quant
        self.__pizzas = pizzas
        self.__precoTotal = precoTotal


    @property
    def nro_pedido(self):
        return self.__nro_pedido

    @property
    def precoTotal(self):
        return self.__precoTotal
    
    @property
    def quant(self):
        return self.__quant
    
    @property
    def pizzas(self):
        return self.__pizzas


class LimiteCadastrarPedido(tk.Toplevel):
    def __init__(self, controle, listaNomes):

        tk.Toplevel.__init__(self)
        self.geometry('350x250')
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
        self.labelPizza.pack(side="top")
        self.escolhaCombo1 = tk.StringVar()
        self.combobox1 = ttk.Combobox(self.framePizza, width = 15 , textvariable = self.escolhaCombo1)
        self.combobox1.pack(side="top")
        self.combobox1['values'] = listaNomes

        self.labelPizza = tk.Label(self.framePizza,text="Escolha o sabor da pizza: ")
        self.labelPizza.pack(side="top")
        self.escolhaCombo2 = tk.StringVar()
        self.combobox2 = ttk.Combobox(self.framePizza, width = 15 , textvariable = self.escolhaCombo2)
        self.combobox2.pack(side="top")
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
        messagebox.showinfo("Pedido ", str)


class ctrlPedido():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPedidos = []

    def cadastrarPedido(self):
        self.listaPizzaTemp = []
        listaNomes = self.ctrlPrincipal.ctrlPizza.getNomePizzas()
        self.limiteCad = LimiteCadastrarPedido(self, listaNomes)

    def consultarPedido(self):
        nroPed = simpledialog.askstring("Consulta de pedido", "Informe o número do pedido: ")
        str1 = ""
        if nroPed:
            for ped in self.listaPedidos:
                if nroPed == ped.nro_pedido:
                    str1 += "Número do pedido: " + ped.nro_pedido + "\n"
                    for ind, pizz in enumerate(ped.pizzas):
                        ind += 1
                        str1 += str(ind) + " " + pizz.descricao + ' ........R$ ' + "{:.2f}".format(float(pizz.preco)) + '\n'
                    str1 += " Total do Pedido: R$ " + "{:.2f}".format(float(ped.precoTotal)) + '\n'
                    self.limiteLista = LimiteConsultarPedido(str1)
                    return
        str1 = "Pedido não encontrado."
        self.limiteLista = LimiteConsultarPedido(str1)


    def inserePizza(self, event):
        sel1 = self.limiteCad.combobox1.current()
        sel2 = self.limiteCad.combobox2.current()

        pizz1 = None  # 
        pizz2 = None

        if sel1 != -1:
            pizzaSel1 = self.limiteCad.escolhaCombo1.get()
            pizz1 = self.ctrlPrincipal.ctrlPizza.getPizza(pizzaSel1)
            self.listaPizzaTemp.append(pizz1)

        if sel2 != -1:
            pizzaSel2 = self.limiteCad.escolhaCombo2.get()
            pizz2 = self.ctrlPrincipal.ctrlPizza.getPizza(pizzaSel2)
            self.listaPizzaTemp.append(pizz2)

        if pizz1 and pizz2:
            self.listaPizzaTemp.remove(pizz1)
            self.listaPizzaTemp.remove(pizz2)
            preco = max(float(pizz1.preco), float(pizz2.preco))
            descricao = pizz1.descricao + ' / ' + pizz2.descricao
            pizzaComb = piz.Pizza('Comb', descricao, preco)
            self.listaPizzaTemp.append(pizzaComb)

        self.limiteCad.combobox1.set('')
        self.limiteCad.combobox2.set('')

        self.limiteCad.mostraJanela('Sucesso', 'Pizza incluída com sucesso')

        

    def fechaPedido(self, event):
        nroPed = self.limiteCad.inputNro_pedido.get()
        quant = self.limiteCad.inputQuant.get()
        precoTotal = 0
        for pizz in self.listaPizzaTemp:
            precoTotal += float(pizz.preco)
        ped = Pedido(nroPed, quant, self.listaPizzaTemp, precoTotal)
        self.listaPedidos.append(ped)
        self.limiteCad.mostraJanela('Sucesso', 'Pedido fechado com sucesso')
        self.limiteCad.destroy()

