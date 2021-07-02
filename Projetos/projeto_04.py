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


def mostrar_candidatos():
    # função para mostrar os candidatos e a quantidade
    # de votos que cada um recebeu

    print(f'''
    --------- ELEIÇÕES 2021 --------

    CANDIDATO           NÚMERO           VOTOS

    {votos[0]['nome']}                  1                  {votos[0]['votos']}
    {votos[1]['nome']}                  2                  {votos[1]['votos']}
    {votos[2]['nome']}                  3                  {votos[2]['votos']}
    {votos[3]['nome']}                   4                  {votos[3]['votos']}
    {votos[4]['nome']}                 5                  {votos[4]['votos']}
    
    ''')


def mostrar_mais_votado():
    # função para mostrar qual candidato possui maior
    # número de votos

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


def autoriza_voto(ano_nascimento):
    # função que calcula a idade do eleitor e retorna
    # se o voto dele é NEGADO, OPCIONAL ou OBRIGATÓRIO

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


def votacao(autoriza_voto, numero):
    # função que checa o status retornado por autoriza_voto()
    # permite a votação e contabiliza o voto no dicionário de
    # votos

    # se o voto do eleitor for OPCIONAL ou OBRIGATÓRIO
    if autoriza_voto in ['OPCIONAL', 'OBRIGATÓRIO']:
        # se o numero do candidato estiver entre 1 e 5
        if numero in range(1, 6):
            # acesso a lista de dicionários de votos transformando o voto
            # em um index e incrementando o valor da chave 'votos'
            votos[numero-1]['votos'] += 1
            print(f'Você votou em {votos[numero-1]["nome"]}!')
        # caso o número informando não esteja entre 1 e 5
        else:
            print('O candidato do número informado não existe')
    # caso o voto do eleitor seja NEGADO
    else:
        print('Você não pode votar.')

if __name__ == '__main__':
    while True:
        system('cls')
        mostrar_candidatos()

        autorizacao = autoriza_voto(int(input('Qual o ano do seu nascimento? ')))
        numero = int(input('\nQual o número do seu candidato? '))

        system('cls')
        votacao(autorizacao, numero)

        mostrar_candidatos()
        mostrar_mais_votado()

        flag = input('Deseja continuar? [S/N] ').strip().upper()
        if flag == 'N':
            break
