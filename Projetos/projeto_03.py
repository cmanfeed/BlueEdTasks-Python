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
from time import sleep
from os import system

# Laço de repetição para manter a execução do jogo
while True:
    # Limpando o terminal pra ficar bonitinho
    system('cls')
    # Dicionário que contém a quantidade de vitórias
    # de cada jogador
    rodadas_vencidas = {1: 0, 2: 0, 3: 0, 4: 0}
    # Leitura da quantidade de rodadas
    rodadas = int(input('Quantas rodadas você deseja? '))
    # Limpando o terminal pra ficar bonitinho
    system('cls')
    # Laço para executar em cada rodada
    r = 1
    while r <= rodadas:
        # Mostra o placar da rodada e o número da rodada
        print(
            f'Rodada {r} | 1️⃣ : {rodadas_vencidas[1]}    | 2️⃣ : {rodadas_vencidas[2]}     | 3️⃣ : {rodadas_vencidas[3]}     | 4️⃣ : {rodadas_vencidas[4]}')
        # 'jogadas' contém a jogada da rodada atual de cada um dos quatro jogadores
        jogadas = choices(range(1, 7), k=4)
        # Mostrar a jogada de cada jogador pra ficar bonitinho
        for j in range(4):
            print(f'\nJogador {j + 1} jogou o 🎲 e deu... {jogadas[j]}!')
            sleep(2.5)
        # Caso apenas um jogador tenha tirado o maior número na rodada
        if jogadas.count(max(jogadas)) == 1:
            # Gravo o index do maior número
            vencedor = jogadas.index(max(jogadas)) + 1
            # Mostrando o vencedor da rodada atual
            print(f'\nO vencedor da rodada é o Jogador {vencedor}!')
            sleep(2)
            # Incremendo a vitória no dicionário de rodadas_vencidas
            rodadas_vencidas[vencedor] = rodadas_vencidas[vencedor] + 1
            # Caso haja um vencedor na rodada, parte pra próxima
            r += 1
        # Caso haja um empate com os maiores números, a rodada é repetida
        else:
            print(f'\nXii... Empatou! Vamos repetir a rodada!')
            sleep(2)
        # Limpando o Terminal
        system('cls')

    # Printa o placar final
    print(
        f'Placar Final | 1️⃣ : {rodadas_vencidas[1]}    | 2️⃣ : {rodadas_vencidas[2]}     | 3️⃣ : {rodadas_vencidas[3]}     | 4️⃣ : {rodadas_vencidas[4]}')
    # Ordenando o dicionário do jogador que teve mais vitórias
    # para o que teve menos vitórias
    rodadas_vencidas = sorted(rodadas_vencidas.items(),
                              key=lambda x: x[1], reverse=True)
    # Printa o vencedor (rodadas_vencidas[0])
    print(
        f'\nO jogador {rodadas_vencidas[0][0]} ganhou {rodadas_vencidas[0][1]} partidas! Ele venceu!')
    # Caso o jogador não queira continuar, termina o jogo
    flag = input('\nDeseja continuar? [S/N] ').strip().upper()
    if flag == 'N':
        break
