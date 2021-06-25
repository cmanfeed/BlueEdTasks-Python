'''
    Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4
    jogadores joguem um dado e tenham resultados aleatórios.
    O programa tem que:
    • Perguntar quantas rodadas você quer fazer
    • Guardar os resultados dos dados em um dicionário.
    • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número
    no dado.
    • Mostrar no final qual jogador ganhou mais rodadas e foi o grande
    campeão.
    Obs: O projeto deve ser feito individualmente e entregue até o final da aula 16.
'''

from random import choices

# Laço de repetição para manter a execução do jogo
while True:
    # Dicionário que contém a quantidade de vitórias
    # de cada jogador
    rodadas_vencidas = {1: 0, 2: 0, 3: 0, 4: 0}

    rodadas = int(input('Quantas rodadas você deseja? '))
    # Laço para executar em cada rodada
    for r in range(rodadas):
        # 'jogadas' contém a jogada da rodada atual de cada um dos quatro jogadores
        jogadas = choices(range(1, 7), k=4)
        # Caso apenas um jogador tenha tirado o maior número na rodada
        if jogadas.count(max(jogadas)) == 1:
            # Gravo o index do maior número
            vencedor = jogadas.index(max(jogadas)) + 1
            # Incremendo a vitória no dicionário de rodadas_vencidas
            rodadas_vencidas[vencedor] = rodadas_vencidas[vencedor] + 1

    # Caso o jogador não queira continuar, termina o jogo
    flag = input('Deseja continuar? [S/N] ').strip().upper()
    if flag == 'N':
        break
