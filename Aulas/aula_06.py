
# '''
#     01 - Faça um programa que pede a senha ao usuário e só sai do looping
#     quando digitarem corretamente a senha
# '''

import random
from time import sleep

senha = input('Informe sua senha: ')
senha_digitada = input('Qual é a sua senha? ')

while senha_digitada != senha:
    print('Senha digitada não confere com a senha original! Tente novamente.')
    senha_digitada = input('Qual é a sua senha? ')

print('Você acertou! Saiu do Loop')

# '''
#     02 - Faça um programa que leia o sexo biológico de uma pessoa, mas só
#     aceite os valores 'M' ou 'F'. Caso esteja errado, peça digitação
#     novamente até ter um valor correto.
# '''

sexo = input('Qual seu sexo biológico? ').strip().upper()[0]

while sexo not in 'MF':
    print('O valor que você informou é inválido! Tente novamente.')
    sexo = input('Qual seu sexo biológico? ').strip().upper()[0]

print('Ok! Você digitou corretamente. Saiu do loop :D')

# '''
#     03 - Crie um jogo onde o computador vai "pensar" em um número entre 0
#     a 10. O jogador vai tentar adivinhar qual número foi escolhido até
#     acertar, mostrando no final quantos palpites foram necessários para vencer.
#     Entre os palpites, diga ao jogador se o número do computador é maior
#     ou menor ao que ele digitou.
# '''

print('O computador está gerando um número... Aguarde...')
numero_pc = random.randint(0, 10)
sleep(2)

chute = int(input(
    '\nNúmero escolhido!\n\nInforme o número que você acha que o computador escolheu: '))
n_tentativas = 1

while chute != numero_pc:
    if chute > numero_pc:
        print('Menor... Tente novamente.')
    else:
        print('Maior... Tente novamente')

    chute = int(
        input('\nInforme o número que você acha que o computador escolheu: '))
    n_tentativas += 1

print(f'Você acertou após {n_tentativas} tentativas. Parabéns!')
