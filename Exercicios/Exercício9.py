n = int(input("Informe a quantidade de pessoas: "))
lista_nomes = []
lista_alturas = []
for i in range(n):
    nome = input(" Digite o nome da pessoa: ")
    lista_nomes.append(nome)
    altura = float(input("Digite a altura desta pessoa: "))
    lista_alturas.append(altura)

mais_alt = lista_alturas[0]
menos_alt = lista_alturas[0]
maior_nome = lista_nomes[0]
menor_nome = lista_nomes[0]

for i in range(1,n):
    if lista_alturas[i] > mais_alt:
        mais_alt = lista_alturas[i]
        maior_nome = lista_nomes[i]
    if lista_alturas[i] < menos_alt:
        menos_alt = lista_alturas[i]
        menor_nome = lista_nomes[i]

print(" O mais alto é {} com altura {}" + maior_nome, mais_alt)
print(" O mais baixo é {} com altura {}" + menor_nome, menos_alt)