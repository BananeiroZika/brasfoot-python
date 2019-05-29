import random
lista = []
print(lista)
contador = 0
while contador < 4:
    lista.append(random.randint(0, 9))
    contador = contador + 1

print(lista)

print('TIME A', lista[0], 'X', lista[1], 'Time B')

if lista[0] > lista[1]:
    print('TIME A VENCEU')
elif lista[0] < lista[1]:
    print('TIME B VENCEU')
else:
    print('EMPATE')

print('Time C', lista[2], 'X',lista[3],'Time D')
if lista[2] > lista[3]:
        print('TIME C GANHOU')
elif lista[2] < lista[3]:
        print('TIME D GANHOU')
else:
        print('EMPATE')
