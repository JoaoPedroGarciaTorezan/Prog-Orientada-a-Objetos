# Definir as exceptions

class UsernameDuplicado(Exception):
    pass

class IdadeMenorQuePermitida(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class EmailInvalido(Exception):
    pass

class User:
    def __init__(self, username, email):
        self.__username = username
        self.__email = email

    def getUsername(self):
        return self.__username

    def getEmail(self):
        return self.__email

if __name__ == "__main__":

    listaExemplo = [
        ("paulo", "paulo@gmail.com", 21),
        ("maria", "maria@gmail.com", 19),
        ("antonio", "antonio@gmail.com", 25),
        ("pedro", "pedro@gmail.com", 15),
        ("marisa", "marisa@", 23),
        ("ana", "ana@gmail.com", -22),
        ("maria", "maria2@gmail.com", 27)
    ]

    cadastro = {}

    for username, email, idade in listaExemplo:
        try:
            if username in cadastro:
                raise UsernameDuplicado()
            if idade < 0:
                raise IdadeInvalida()
            if idade < 18:
                raise IdadeMenorQuePermitida()
            emailPartes = email.split("@") #split -> separa a string em partes, usando o caractere "@" como delimitador
            if len(emailPartes) != 2 or not emailPartes[0] or not emailPartes[1]:
                raise EmailInvalido()
        except UsernameDuplicado:
            print(f"Erro: O username '{username}' já está em uso.")
        except IdadeInvalida:
            print(f"Erro: A idade '{idade}' é inválida.")
        except IdadeMenorQuePermitida:
            print(f"Erro: A idade de '{username}' é menor que a permitida.")
        except EmailInvalido:
            print(f"Erro: O email '{email}' é inválido.")
        else:
            cadastro[username] = User(username, email)