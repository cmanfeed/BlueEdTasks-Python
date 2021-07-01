
# Projeto 04 - Simulador de votação:

# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:

# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.

# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização(que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.

# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):

#     ● 1, 2 ou 3 - Votos para os respectivos candidatos
#     ● 4 - Voto Nulo
#     ● 5 - Voto em Branco

# Sua função votacao() tem que calcular e mostrar:

#     ● O total de votos para cada candidato
#     ● O total de votos nulos
#     ● O total de votos em branco
#     ● Qual candidato venceu a votação

from os import system

# 'votos' será um dicionário que irá conter os
# participantes da eleição e a quantidade de voto
# que cada um receber
votos = [
    {'nome': 'Chico', 'votos': 0},
    {'nome': 'André', 'votos': 0},
    {'nome': 'Carla', 'votos': 0},
    {'nome': 'Nulo', 'votos': 0},
    {'nome': 'Branco', 'votos': 0},
]

# função para mostrar os candidatos e a quantidade
# de votos que cada um recbeu
def mostrar_candidatos():
    print(f'''
    --------- ELEIÇÕES 2021 --------

    CANDIDATO           NÚMERO           VOTOS

    {votos[0]['nome']}                  1                  {votos[0]['votos']}
    {votos[1]['nome']}                  2                  {votos[1]['votos']}
    {votos[2]['nome']}                  3                  {votos[2]['votos']}
    {votos[3]['nome']}                   4                  {votos[3]['votos']}
    {votos[4]['nome']}                 5                  {votos[4]['votos']}
    
    ''')

# função para mostrar qual candidato possui maior
# número de votos
def mostrar_mais_votado():
    # assume que o mais votado é o primeiro candidato
    mais_votado = votos[0]
    # percorre o dicionário de candidatos e votos
    for candidato in votos:
        # caso exista algum candidato que tenha mais votos
        # que o 'mais_votado', esse candidato se torna o mais votado
        if candidato['votos'] > mais_votado['votos']:
            mais_votado = candidato
    # mostra o candidato mais votado
    print(
        f'\n-----> Vencedor até o momento: {mais_votado["nome"]} com {mais_votado["votos"]} Votos! <-----\n')

# função que calcula a idade do eleitor e retorna
# se o voto dele é NEGADO, OPCIONAL ou OBRIGATÓRIO
def autoriza_voto(ano_nascimento):
    from datetime import date
    # calculo a idade com base no ano atual
    idade = date.today().year - ano_nascimento
    # caso o eleitor tenha menos que 16 anos
    if idade < 16:
        return f'NEGADO'
    # caso o eleitor tenha de 16 a 18 anos ou 
    # mais que 70 anos
    elif idade in range(16, 19) or idade > 70:
        return f'OPCIONAL'
    # todo o resto
    else:
        return f'OBRIGATÓRIO'

# função que checa o status retornado por autoriza_voto()
# permite a votação e contabiliza o voto no dicionário de
# votos
def votacao(autoriza_voto, numero):
    # se o voto do eleitor for OPCIONAL ou OBRIGATÓRIO
    if autoriza_voto in ['OPCIONAL', 'OBRIGATÓRIO']:
        # se o numero do candidato estiver entre 1 e 5
        if numero in range(1, 6):
            # acesso a lista de dicionários de votos transformando o voto
            # em um index e incrementando o valor da chave 'votos'
            votos[numero-1]['votos'] += 1
            print(f' Você votou em {votos[numero-1]["nome"]}! ')
        # caso o número informando não esteja entre 1 e 5
        else:
            print('O candidato do número informado não existe')
    # caso o voto do eleitor seja NEGADO
    else:
        print('Você não pode votar.')


while True:
    system('cls')
    mostrar_candidatos()

    autorizacao = autoriza_voto(int(input('Qual o ano do seu nascimento? ')))
    numero = int(input('\nQual o número do seu candidato? '))

    system('cls')
    votacao(autorizacao, numero)

    mostrar_candidatos()
    mostrar_votos()

    flag = input('Deseja continuar? [S/N] ').strip().upper()
    if flag == 'N':
        break
