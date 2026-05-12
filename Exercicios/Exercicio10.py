from datetime import datetime

#Converte os parametros de horas, minutos e segundos em segundos. Retorna o valor em segundos
def Conversao_segundos(h, min, s):
    seg = h * 3600 + min * 60 + s
    return seg
#Converte o paraemtro segundos em hora, minuto e segundo
def Conversao_hora_minuto_segundo(s):
    horas = s // 3600 # // -> retorna a parte inteira de uma divisão
    min = (s % 3600) // 60
    seg = s % 60
    return [horas, min, seg]

print(" Informe o horario de conexão: ")
horaC = int(input("Hora da Conexão: "))
minC = int(input("Minuto da Conexão: "))
segC = int(input("Segundo da Conexão: "))

print(" Informe o horário da desconexão: ")
horaD = int(input("Hora da Desconexão: "))
minD = int(input("Minuto da Desconexão: "))
segD = int(input("Segundo da Desconexão: "))

tempo_total = Conversao_segundos(horaD,minD,segD) - Conversao_segundos(horaC,minC,segC)
tempo_total_hms = Conversao_hora_minuto_segundo(tempo_total) 
print(" O tempo que o usuário ficou conectado no sistema foi de " + str(tempo_total_hms[0]) + " h " + str(tempo_total_hms[1]) + " min " + str(tempo_total_hms[2]) + " s ")