import tkinter as tk
import medico as med #passa os outros programas
import consulta as cons

#Observações:
# Model - dados
# View - interface do usuário
# Frames - organização visual da interface, agrupando elementos relacionados.
# Label - rótulos de texto para identificar campos ou fornecer informações.
# Entry - campos de entrada de dados
# Button - botões para acionar ações
# Bind - vincula eventos (como cliques) a funções de callback
# Controller - lógica de controle, manipula eventos e interage com o modelo e a view
# root - janela principal da aplicação

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.MedicoMenu = tk.Menu(self.menubar)
        self.ConsultaMenu = tk.Menu(self.menubar)
        self.PlaylistMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)
        
        self.MedicoMenu.add_command(label="Cadastrar", command=self.controle.cadastraMedico)
        self.MedicoMenu.add_command(label="Listar", command=self.controle.listagemConsulta)
        self.menubar.add_cascade(label="Médico", menu=self.MedicoMenu)

        self.ConsultaMenu.add_command(label="Cadastrar", command=self.controle.cadastraConsulta)
        self.menubar.add_cascade(label="Consulta", menu=self.ConsultaMenu)
        self.root.config(menu=self.menubar)

        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlMedico = med.CtrlMedico() #passa o controle principal

        self.ctrlConsulta = cons.CtrlConsulta(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Clínica Médica")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastraMedico(self):
        self.ctrlMedico.cadastraMedico()

    def listagemConsulta(self):
        self.ctrlMedico.listagemConsulta()

    def cadastraConsulta(self):
        self.ctrlConsulta.cadastraConsulta()
    
    def salvaDados(self):
        self.ctrlMedico.salvaMedicos()
        # pode colocar mais coisa para salvar
        self.root.destroy()

    
if __name__ == '__main__':
    c = ControlePrincipal()