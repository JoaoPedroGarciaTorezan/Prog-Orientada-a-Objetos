#Definir exceptions

class TitulacaoInvalida(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class IdadeMenorQuePermitida(Exception):
    pass

class CPFInvalido(Exception):
    pass

class Pessoa():
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def cpf(self):
        return self.__cpf
    
    def printDescricao(self):
        print(f"Nome: {self.__nome}")
        print(f"Endereço: {self.__endereco}")
        print(f"Idade: {self.__idade}")
        print(f"CPF: {self.__cpf}")

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao
    
    @property
    def titulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        super().printDescricao()
        print(f"Titulação: {self.__titulacao}")

class Aluno(Pessoa): 
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso
    
    def printDescricao(self):
        super().printDescricao()
        print(f"Curso: {self.__curso}")

if __name__ == "__main__":
    cadastro = {}
    listaExemplo = []

    Professor1 = Professor("Minoru", "Rua A", 67, "123.456.789-00", "Mestrado")
    listaExemplo.append(Professor1)
    Professor2 = Professor("Melise", "Rua B", 45, "987.654.321-00", "Doutorado")
    listaExemplo.append(Professor2)
    Aluno1 = Aluno("Fábio", "Rua C", 24, "111.222.333-44", "Engenharia")
    listaExemplo.append(Aluno1)
    Aluno2 = Aluno("Ana", "Rua D", 16, "555.666.777-88", "CCO")
    listaExemplo.append(Aluno2)
    Professor3 = Professor("Aurelio", "Rua E", 27, "999.888.777-66", "Doutorado")
    listaExemplo.append(Professor3)
    Aluno3 = Aluno("Maria", "Rua F", 20, "444.555.666-77", "SIN")
    listaExemplo.append(Aluno3)
    Aluno4 = Aluno("João", "Rua G", 19, "222.333.444-55", "CCO")
    listaExemplo.append(Aluno4)
    Professor4 = Professor("Carlos", "Rua H", 30, "12345678900", "Doutorado")
    listaExemplo.append(Professor4)
    Aluno5 = Aluno("Pedro", "Rua J", 20, "12345678900", "SIN")
    listaExemplo.append(Aluno5)

    for pessoa in listaExemplo:
        try:
            if pessoa.cpf in cadastro:
                raise CPFInvalido()
            if isinstance(pessoa, Professor):
                if pessoa.idade < 30:
                    raise IdadeInvalida()
                if pessoa.titulacao != 'Doutorado':
                    raise TitulacaoInvalida()
            if isinstance(pessoa, Aluno):
                if pessoa.idade < 18:
                    raise IdadeMenorQuePermitida()
                if pessoa.curso not in ['CCO', 'SIN']:
                    raise CursoInvalido()
        except CPFInvalido:
            print("Erro ao cadastrar {}: O CPF {} já está em uso.".format(pessoa.nome, pessoa.cpf))
        except IdadeInvalida:
            print("Erro ao cadastrar {}: {} anos é menos que a idade mínima permitida para um professor.".format(pessoa.nome, pessoa.idade))
        except TitulacaoInvalida:
            print("Erro ao cadastrar {}: {} não é permitido para o cadastro.".format(pessoa.nome, pessoa.titulacao))
        except IdadeMenorQuePermitida:
            print("Erro ao cadastrar {}: {} anos é menos que a idade mínima permitida para um aluno.".format(pessoa.nome, pessoa.idade))
        except CursoInvalido:
            print("Erro ao cadastrar {}: {} não é um curso permitido para o cadastro.".format(pessoa.nome, pessoa.curso))
        else:
            cadastro[pessoa.cpf] = pessoa

    print("\nPessoas cadastradas com sucesso:\n")
    for pessoa in cadastro:
        cadastro[pessoa].printDescricao()
        print()


