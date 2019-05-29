import random
lista = []
times = ['Barcelona' ,'São Paulo', 'Milan', 'River Plate']
print(times[0])
#vou tentar fazer a adição de numeros a matriz utilizando função
def sorteio(a, b):

    resp = random.randint(a, b)
    return resp

def comparar(golstime1, golstime2,nomedotime):
    if golstime1 > golstime2:
        return print('O', nomedotime, 'Venceu')
    elif golstime1 < golstime2:
        return print('O', nomedotime, 'PERDEU')
    else:
        return "Empate"

timea = sorteio(0, 9)
print(timea)

contador = 0
while contador < 4:
    lista.append(random.randint(0, 9))
    contador = contador + 1

                                                    # JOGOS
#JOGO 1
print(times[0], timea, 'X', lista[1], times[1])
    #COMPARAR RESULTADOS
print(comparar(timea, lista[1],times[0]))
#JOGO 2
print(times[2], lista[2], 'X',lista[3], times[3])
    #COMPARAR RESULTADOS
print(comparar(lista[2], lista[3], times[2]))
