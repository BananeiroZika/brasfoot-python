import os

lista = []
arquivo = open("times.csv", "r")
lista = arquivo.readlines()
arquivo.close()

opcao = 0

def menu():
    print("\n","="*30)
    print('''    1-Cadastrar time
    2-Editar
    ''')

def comando():
    opcao = input('Digite o Comando')
    return opcao

def lista_times(nome, opcao):
    if(opcao=='1'):
        clube = nome+"\n"
        lista.append(clube)
        lista.sort()
        arquivo = open("times.csv", 'w')
        tam = len(lista)

        for i in range(tam):
            arquivo.write(lista[i])

        arquivo.close()
        print('Time cadastrado!')
    else:
        print('err0r')


menu()
opcao = comando()

if opcao == '1':
    nome = str(input("Nome do time:"))
    lista_times(nome,'1')
elif opcao == '2':
    print('Função não adicionada')
else:
    print("Digite uma função existente")
