import random
import csv

#dicionarios e listas
times = []
timesjogando = []

#ABRIR BANCO DE TIMES
arquivo = open('times.csv','r')
times = arquivo.readlines()
arquivo.close()

#FUNÇÕES
def sorteio():

    resp = random.randint(0, 5)
    return resp

def jogo(partipantes,contador_externo, divisao):
    contador = contador_externo
    timecasa = 0
    timefora = 0
    print("="*20)
    participantes_divisao = divisao
    while contador < participantes:
        timecasa = sorteio()
        timefora = sorteio()
        print(timesjogando[contador], timecasa, ' x ', timefora, timesjogando[contador + 1])
        if timefora < timecasa:
            if participantes_divisao > 1:
                timesjogando.append(timesjogando[contador])
        elif timefora > timecasa:
            if participantes_divisao > 1:
                timesjogando.append(timesjogando[contador+1])
        else:
            if participantes_divisao > 1:
                timesjogando.append(timesjogando[contador])
        contador = contador+2

min_times = 2
participantes = 2

participantes = int(input('Digite o numero de times (2 - 4 - 8):'))

for i in range(participantes):
        #RESOLVER QUEBRAS DE LINHA
        jogar = times[i]
        timesjogando.append(jogar.strip('\n'))

# ====== COMEÇO REAL =========

contador = 0
contador_b = 1
    #NUMERO DE FASES
participantes_divisao = participantes
while participantes_divisao/2 > 1:
    contador_b = contador_b+1
    participantes_divisao = participantes_divisao/2



while contador_b > 0:
    jogo(participantes,contador, contador_b)
    contador = participantes
    participantes = len(timesjogando)
    sobra = participantes - contador
    contador_b = contador_b - 1


campeao = len(timesjogando)
print('1º ',timesjogando[campeao-1])

print('2º ',timesjogando[campeao-2])

print('3º ',timesjogando[campeao-3])

print('O CAMPEÃO :', timesjogando[campeao-1])

salvar = input('\nDeseja Salvar seu campeonato?')
if salvar == 'sim':
    salve = open('teste.txt','w')
