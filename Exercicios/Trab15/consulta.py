import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import os.path
import pickle

class Consulta:
    def __init__(self, nomePac, dia, hora, especialidade, medico):
        self.__nomePac = nomePac
        self.dia = dia
        self.hora = hora
        self.__especialidade = especialidade
        self.__medico = medico

    @property
    def nomePac(self):
        return self.__nomePac
    
    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, valor):
        if valor < 1 or valor > 30:
            raise ValueError("Dia inválido: {}".format(valor))
        else:
            self.__dia = valor
    
    @property
    def hora(self):
        return self.__hora
    
    @hora.setter
    def hora(self, valor):
        if valor < 9 or valor > 17:
            raise ValueError("Hora inválida: {}".format(valor))
        else:
            self.__hora = valor

    @property
    def especialidade(self):
        return self.__especialidade
    
    @property
    def medico(self):
        return self.__medico

    
class limiteInsConsulta(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('350x250')
        self.title("Consulta")
        self.controle = controle

        self.framenomePac = tk.Frame(self)
        self.frameDia = tk.Frame(self)
        self.frameHora = tk.Frame(self)
        self.frameEspecialidade = tk.Frame(self)
        self.frameMedico = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framenomePac.pack()
        self.frameDia.pack()
        self.frameHora.pack()
        self.frameEspecialidade.pack()
        self.frameMedico.pack()
        self.frameButton.pack()
      
        self.labelnomePac = tk.Label(self.framenomePac, text="Nome do paciente: ")
        self.labelnomePac.pack(side="left")
        self.inputnomePac = tk.Entry(self.framenomePac)
        self.inputnomePac.pack(side="left")

        self.labelDia = tk.Label(self.frameDia, text="Informe o dia: ")
        self.labelDia.pack(side="left")
        self.inputDia = tk.Entry(self.frameDia)
        self.inputDia.pack(side="left")

        self.labelHora = tk.Label(self.frameHora, text="Informe o horário: ")
        self.labelHora.pack(side="left")
        self.inputHora = tk.Entry(self.frameHora)
        self.inputHora.pack(side="left")

        self.labelEspecialidade = tk.Label(self.frameEspecialidade,text="Escolha a especialidade: ")
        self.labelEspecialidade.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameEspecialidade, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = ["Pediatra", "Cardiologia", \
                            "Neurologia", "Oftalmologia", "Ortopedia", \
                            "Gastroenterologia", "Psiquiatria", "Pneumologia"]
        self.combobox.bind("<<ComboboxSelected>>", self.controle.exibeEspecialidade)

        self.labelMedico = tk.Label(self.frameMedico,text="Escolha o médico: ")
        self.labelMedico.pack(side="left") 
        self.listbox = tk.Listbox(self.frameMedico)
        self.listbox.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastra a consulta")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.insereConsulta)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Limpa")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  


    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
    
class CtrlConsulta:
    def __init__(self, controlePrincipal):
        self.listaConsultas = []
        self.ctrlPrincipal = controlePrincipal

    def cadastraConsulta(self):
        self.limiteIns = limiteInsConsulta(self)

    def insereConsulta(self, event):
        nomePac = self.limiteIns.inputNome.get()
        dia = int(self.limiteIns.inputDia.get())
        hora = int(self.limiteIns.inputHora.get())
        espcSel = self.limiteIns.combobox.get()
        especialidade = self.ctrlPrincipal.ctrlMedico.getEspecialidade(espcSel)
        medSel = self.limiteIns.listbox.get(tk.ACTIVE)
        medico = self.ctrlPrincipal.ctrlMedico.getMedico(medSel)
        try:
            consulta = Consulta(nomePac, dia, hora, especialidade, medico)
            self.listaConsultas.append(consulta)
            self.limiteIns.mostraJanela("Sucesso", "Consulta cadastrada com sucesso!")
            self.clearHandler(event)
        except ValueError as error:
            self.limiteIns.mostraJanela("Erro", error)

    def clearHandler(self, event):
        self.limiteIns.inputnomePac.delete(0, len(self.limiteIns.inputnomePac.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def exibeEspecialidade(self, event):
        espcSel = self.limiteIns.combobox.get()
        especialidade = self.ctrlPrincipal.ctrlMedico.getEspecialidade(espcSel)
        listaMedicos = self.ctrlPrincipal.ctrlMedico.getListaMedicos()
        self.limiteIns.listbox.delete(0, tk.END)
        for med in listaMedicos:
            if med.especialidade == especialidade:
                self.limiteIns.listbox.insert(tk.END, med.nome)
