from datetime import datetime #classe datetime
hoje = datetime.now() #metodo (now) 
print('Hoje é: ' + str(hoje)) #objeto: var hoje
print('-----')
print('Dia: ' + str(hoje.day)) #day: propriedade do obj hoje
print('Mes: ' + str(hoje.month))
print('Dia: ' + str(hoje.year))
print('-----')
print('Dia da semana: ' + str(hoje.weekday()))
ontem = datetime(2026, 3, 8)
print('Dia da semana: ' + str(ontem.weekday()))
print('-----')
dias = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
nome_dia = dias[hoje.weekday()]
print('Dia da semana: ' + nome_dia)