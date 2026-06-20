import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import os.path
import pickle

class Medico:
    def __init__(self, nome, CRM, especialidade):
        self.__nome = nome
        self.__CRM = CRM
        self.especialidade = especialidade
        self.__consultas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def CRM(self):
        return self.__CRM
    
    @property
    def especialidade(self):
        return self.__especialidade
    
    @especialidade.setter
    def especialidade(self, espc):
        self.especialidades = ["Pediatra", "Cardiologia", \
                            "Neurologia", "Oftalmologia", "Ortopedia", \
                            "Gastroenterologia", "Psiquiatria", "Pneumologia"]
        if espc not in self.especialidades:
            raise ValueError("Especialidade inválida: {}".format(espc))
        else:
            self.__especialidade = espc

    @property
    def consultas(self):
        return self.__consultas
    
    def addConsulta(self, consulta):
        self.consultas.append(consulta)

    def infoMedico(self):
        str = ""
        for cons in self.consultas:
            str += "{} / {} / {} \n".format(cons.dia,cons.hora,cons.nomePac)
        return str

    
class limiteInsMedico(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Médico")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCRM = tk.Frame(self)
        self.frameEspecialidade = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameCRM.pack()
        self.frameEspecialidade.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome)
        self.inputNome.pack(side="left")

        self.labelCRM = tk.Label(self.frameCRM, text="CRM: ")
        self.labelCRM.pack(side="left")
        self.inputCRM = tk.Entry(self.frameCRM)
        self.inputCRM.pack(side="left")

        self.labelEspecialidade = tk.Label(self.frameEspecialidade, text="Especialidade: ")
        self.labelEspecialidade.pack(side="left")
        self.inputEspecialidade = tk.Entry(self.frameEspecialidade)
        self.inputEspecialidade.pack(side="left")

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

class LimiteListagemConsulta(tk.Toplevel):
    def __init__(self, controle, listaNomes):

        tk.Toplevel.__init__(self)
        self.geometry('350x300')
        self.title("Listagem de Consulta dos médicos")
        self.controle = controle

        self.frameMedico = tk.Frame(self)
        self.frameConsultas = tk.Frame(self)
        self.frameMedico.pack()
        self.frameConsultas.pack(pady=3)

        self.labelMedico = tk.Label(self.frameMedico,text="Escolha o médico: ")
        self.labelMedico.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameMedico, width = 15 , values=listaNomes, textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox.bind("<<ComboboxSelected>>", self.controle.exibeConsultas)

        self.textConsultas = tk.Text(self.frameConsultas, height=20, width=40)
        self.textConsultas.pack(side='left')
        self.textConsultas.config(state=tk.DISABLED)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
    
class CtrlMedico:
    def __init__(self):
        if not os.path.isfile("medicos.pickle"):
            self.listaMedicos = []
        else:
            try:
                with open("medicos.pickle", "rb") as m:
                    self.listaMedicos = pickle.load(m)
            except EOFError as error:
                self.listaMedicos = []

    def salvaMedicos(self):
        if len(self.listaMedicos) != 0:
            with open("medicos.pickle", "wb") as m:
                pickle.dump(self.listaMedicos, m)

    def getListaNomesMedicos(self):
        listNomes = []
        for med in self.listaMedicos:
            listNomes.append(med.nome)
        return listNomes
    
    def getEspecialidade(self, esp):
        for med in self.listaMedicos:
            if med.especialidade == esp:
                return med
    
    def getMedico(self, medico):
        for med in self.listaMedicos:
            if medico == med.nome:
                return med
            
    def getListaMedicos(self):
        return self.listaMedicos

    def cadastraMedico(self):
        self.limiteIns = limiteInsMedico(self)

    def listagemConsulta(self):
        listNomes = self.getListaNomesMedicos()
        self.limiteCons = LimiteListagemConsulta(self, listNomes)

    def enterHandler(self, event):
        Nome = self.limiteIns.inputNome.get()
        CRM = self.limiteIns.inputCRM.get()
        espc = self.limiteIns.inputEspecialidade.get()
        try:
            medico = Medico(Nome, CRM, espc)
            self.listaMedicos.append(medico)
            self.limiteIns.mostraJanela("Sucesso", "Médico cadastrado com sucesso!")
            self.clearHandler(event)
        except ValueError as error:
            self.limiteIns.mostraJanela("Erro", error)
    
    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, tk.END)
        self.limiteIns.inputCRM.delete(0, tk.END)
        self.limiteIns.inputEspecialidade.delete(0, tk.END)

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def exibeConsultas(self, event):
        medSel = self.limiteCons.combobox.get()
        self.limiteCons.textConsultas.config(state='normal')
        self.limiteCons.textConsultas.delete(1.0, tk.END)
        for med in self.listaMedicos:
            if med.nome == medSel:
                self.limiteCons.textConsultas.insert(1.0, med.infoMedico() + "\n\n")
        self.limiteCons.textConsultas.config(state='disabled')
