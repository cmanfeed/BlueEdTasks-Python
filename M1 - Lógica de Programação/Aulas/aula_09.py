'''
    # 01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
    cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
    adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
    crescente.
'''

from random import sample

lista = list()

while True:
    n = int(input('Informe um valor numérico: '))

    if n not in lista:
        lista.append(n)

    flag = input('Deseja Continuar? [S/N] :').strip().upper()[0]

    if flag == 'N':
        break

lista.sort()
print(f'Lista gerada: {lista}')

'''
    # 02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
    disso, crie duas listas extras que vão conter apenas os valores pares e os valores
    ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
    geradas.
'''

lista = list()
pares = list()
impares = list()

while True:
    numero = int(input('\nInforme um valor numérico: '))

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    lista.append(numero)

    flag = input('Deseja Continuar? [S/N] :').strip().upper()[0]
    if flag == 'N':
        break

print(f'''
Lista Original      : {lista}
Lista com Pares     : {pares}
Lista com Ímpares   : {impares}
''')

'''
    Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
    palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
    números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

sorteados_jogos = list()

n_jogos = int(input('Quantos jogos você deseja jogar? '))

for i in range(n_jogos):
    sorteados_jogos.append(sample(range(1, 60), 6))

for i, sorteado in enumerate(sorteados_jogos):
    print(f'{i + 1}º lista sorteada: {sorteado}')
