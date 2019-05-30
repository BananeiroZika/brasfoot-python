import random
lista = []
times = []
timesjogando = []
arquivo = open("times.csv", "r")
times = arquivo.readlines()
arquivo.close()
tam = len(times)
for i in range(tam):
    jogar = times[i]
    print(jogar.strip('\n'))
    timesjogando.append(jogar.strip('\n'))
    print(timesjogando)

#vou tentar fazer a adição de numeros a matriz utilizando função
def sorteio():

    resp = random.randint(0, 5)
    return resp

def comparar(golstime1, golstime2,nomedotime):
    if golstime1 > golstime2:
        return print('O ', nomedotime, 'Venceu')
    elif golstime1 < golstime2:
        return print('O', nomedotime, 'PERDEU')
    else:
        return "Empate"


contador = 0
while contador < 4:
    lista.append(random.randint(0, 9))
    contador = contador + 1

timea = sorteio()
timeb = sorteio()
timec = sorteio()
timed = sorteio()
final1 = sorteio()
final2 = sorteio()
# JOGOS
print('='*15,'SEMIFINAL:','='*15)
print(timesjogando[1],timea,'X',timeb, timesjogando[0])
print(timesjogando[2],timec,'X',timed,timesjogando[3])
if timea > timeb:
    finalista1 = timesjogando[1]
elif timea == timeb:
    finalista1 = timesjogando[0]
else:
    finalista1 = timesjogando[0]

if timec > timed:
    finalista2 = timesjogando[2]
elif timec == timed:
    finalista2 = timesjogando[3]
else:
    finalista2 = timesjogando[3]

print('='*15,'FINAL:','='*15)
print(finalista2, final1 ,'X', final2, finalista1)
