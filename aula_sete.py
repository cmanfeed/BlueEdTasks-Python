from time import sleep
from random import randint
'''
    #01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
    o maior e o menor peso lidos.
'''
menor = maior = float(input('Informe o peso da 1º pessoa: '))

for i in range(2, 6):
    n = float(input(f'Informe o peso da {i}º pessoa: '))
    if n > maior:
        maior = n

    if n < menor:
        menor = n

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')

'''
    #02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
    tabuada desse número.
'''

n = int(input('Informe um número inteiro para o cálculo da tabuada: '))

for i in range(1, 11):
    print(f'{i} x {n} = {i*n}')

'''
    #03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
    mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
    maiores.
'''

menoridade = maioridade = 0

for i in range(1, 8):
    ano_nascimento = int(
        input(f'Informe o ano de nascimento da {i}° pessoa: '))

    if 2021 - ano_nascimento >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f'Quantidade de pessoas com maioridade: {maioridade}')
print(f'Quantidade de pessoas com menoridade: {menoridade}')

'''
    #04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
    apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
    Mostre também quantos valores pares foram digitados.
'''

soma_pares = pares = 0

for i in range(1, 7):
    n = int(input(f'Informe o {i}º número inteiro: '))

    if n % 2 == 0:
        soma_pares += n
        pares += 1

print(f'Você digitou {pares} números pares.')
print(f'A soma dos números pares digitados é {soma_pares}.')

'''
    #05 - Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)
'''

n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))
op = 0

while op != 5:

    print('''
    
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    
    ''')

    op = int(input('Informe a opção desejada: '))

    if op == 1:
        print(f'A soma é: {n1} + {n2} = {n1 + n2}')

    elif op == 2:
        print(f'A multiplicação é: {n1} * {n2} = {n1 * n2}')

    elif op == 3:
        if n1 > n2:
            print(f'O maior número é o primeiro digitado, {n1}')
        elif n2 > n1:
            print(f'O maior número é o segundo digitado, {n2}')
        else:
            print('Os números digitados são iguais!')

    elif op == 4:
        n1 = float(input('Informe o primeiro valor: '))
        n2 = float(input('Informe o segundo valor: '))
        print('Números atualizados!')

    else:
        print('O valor informado é inválido.')

'''
    #06 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
    pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
    continuar. No final, mostre:
    A) Quantas pessoas têm mais de 18 anos.
    B) Quantos homens foram cadastrados.
    C) Quantas mulheres têm menos de 20 anos.
'''

maioridade = homens = mulheres_menoridade = 0

while True:
    idade = int(input('\nInforme sua idade: '))
    sexo = input('Informe seu sexo [F/M]: ').strip().upper()[0]

    if idade > 18:
        maioridade += 1

    if sexo == 'M':
        homens += 1

    if idade < 20 and sexo == 'F':
        mulheres_menoridade += 1

    flag = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if flag == 'N':
        break

print(f'\nQuantas pessoas têm mais de 18 anos? {maioridade} pessoas.')
print(f'Quantos homens foram cadastrados? {homens} homens.')
print(
    f'Quantas mulheres têm menos de 20 anos? {mulheres_menoridade} mulheres.')

'''
    #07 - Crie um programa que leia o nome e o preço de vários produtos. O programa
    deverá perguntar se o usuário vai continuar ou não. No final, mostre:
    A) Qual é o total gasto na compra.
    B) Quantos produtos custam mais de R$1000.
    C) Qual é o nome do produto mais barato.
'''

total = mais_de_mil = 0
qtd_while = 1
flag = 'S'

while flag != 'N':
    qtd_while += 1

    nome = input('\nInforme o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))

    total += preco

    if preco > 1000:
        mais_de_mil += 1

    if qtd_while == 1:
        produto_mais_barato = nome
        preco_mais_barato = preco

    elif preco < preco_mais_barato:
        produto_mais_barato = nome
        preco_mais_barato = preco

    flag = input('Deseja continuar? [S/N]: ').strip().upper()[0]

print(f'\nTotal gasto: {total}')
print(f'Quantidade de produtos que custam mais de R$ 1000: {mais_de_mil}')
print(f'Produto mais barato: {produto_mais_barato}')

'''
    #08 (DESAFIO) Crie um jogo onde o computador vai “pensar” em um número entre
    0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os
    palpites diga ao jogador se o número do computador é maior ou menor ao que ele
    digitou, no final mostre quantos palpites foram necessários para vencer.
'''

print('O computador está pensando em um número... Aguarde...')
sleep(2)
numero_pc = randint(0, 10)
print('\nNúmero pensado! Tente adivinhar agora.')

tentativas = 1
while True:
    numero_usuario = int(
        input('Qual número você acha que o computador pensou? [0 - 10]: '))

    if numero_usuario > numero_pc:
        print('Menos do que isso...\n')
        tentativas += 1
    elif numero_usuario < numero_pc:
        print('Mais que isso...\n')
        tentativas += 1
    else:
        print('Você acertou! Parabéns!')
        print(f'\nE levou {tentativas} tentativas para conseguir :)')
        break

'''
    #09 (DESAFIO) Em uma eleição presidencial existem quatro candidatos. Os votos
    são informados por meio de código.
    Os códigos utilizados são:
    1, 2, 3 - Votos para os respectivos candidatos
    (você deve montar a tabela ex: 1 - José / 2 - João / etc)
    5 - Voto Nulo
    6 - Voto em Branco
    Faça um programa que calcule e mostre:
    O total de votos para cada candidato
    O total de votos nulos
    O total de votos em branco
    A percentagem de votos nulos sobre o total de votos
    A percentagem de votos em branco sobre o total de votos.
'''

votos_jose = votos_joao = votos_cleiton = 0
votos_nulo = votos_branco = total_votos = 0

while True:
    print('''
    --------------- ELEIÇÕES 2021 --------------- 
    Fala cidadão! Vote em uma das opções a seguir:

    [1] - José de Belém
    [2] - João Gafanhoto
    [3] - Cleiton da Silva
    [5] - Nulo
    [6] - Branco
    [7] - Sair

    ''')

    op = int(input('Informe sua opção: '))

    if op == 1:
        print('Você Votou em José de Belém!\n')
        votos_jose += 1

    elif op == 2:
        print('Você Votou em João Gafanhoto!\n')
        votos_joao += 1

    elif op == 3:
        print('Você Votou em Cleiton da Silva!\n')
        votos_cleiton += 1

    elif op == 5:
        print('Você Votou Nulo!\n')
        votos_nulo += 1

    elif op == 6:
        print('Você Votou Branco!\n')
        votos_branco += 1

    elif op == 7:
        break

    total_votos += 1

print(f'''
    --- APURAÇÃO PARCIAL DOS VOTOS ---
    
    [1] - José de Belém         : {votos_jose} Votos
    [2] - João Gafanhoto        : {votos_joao} Votos
    [3] - Cleiton da Silva      : {votos_cleiton} Votos
    [5] - Nulo                  : {votos_nulo} Votos
    [6] - Branco                : {votos_branco} Votos

    Percentual de Votos Nulos   : {votos_nulo/total_votos:.2f}%
    Percentual de Votos Brancos : {votos_branco/total_votos:.2f}%

''')
