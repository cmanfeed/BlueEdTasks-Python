'''
    Utilizando os conceitos aprendidos até estruturas de repetição, crie um
    programa que jogue pedra, papel e tesoura(Jokenpô) com você.
    O programa tem que:
    • Permitir que eu decida quantas rodadas iremos fazer
    • Ler a minha escolha(Pedra, papel ou tesoura)
    • Decidir de forma aleatória a decisão do computador
    • Mostrar quantas rodadas cada jogador ganhou
    • Determinar quem foi o grande campeão de acordo com a quantidade de
    vitórias de cada um(computador e jogador)
    • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
    de quantidade de rodadas, se não finalize o programa.
    
    Obs: O projeto deve ser feito individualmente e entregue até o final da aula 11.
'''

from random import choice
from time import sleep
from os import system

pedra_icon = '\U0001F5FF'
papel_icon = '\U0001F4C4'
tesou_icon = '\U00002702'
lagar_icon = '\U0001F41B'
spock_icon = '\U0001F596'

jogad_icon = '\U0001F913'
compu_icon = '\U0001F4BB'

jogadas = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']

while True:
    system('cls')
    qtd_rodadas = int(input('Quantas rodadas tu queres? '))

    jogador_venceu = computador_venceu = 0

    system('cls')
    for i in range(qtd_rodadas):
        print(
            f'\nRODADA {i+1} ---- {jogad_icon} {jogador_venceu} X {compu_icon} {computador_venceu}')

        jogador = int(input(
            f'\nQual sua escolha?\n\n[1] - Pedra   {pedra_icon}\n[2] - Papel   {papel_icon}\n[3] - Tesoura {tesou_icon}\n[4] - Lagarto {lagar_icon}\n[5] - Spock   {spock_icon}\n\nDigite sua escolha: '))

        computador = choice(jogadas)
        jogador = jogadas[jogador-1]

        if jogador == 'Pedra':
            system('cls')

            if computador == 'Papel':
                print(
                    f'\nVocê: {pedra_icon} x Computador: {papel_icon}\n\n-- Papel Cobre Pedra --\n\nComputador Ganhou!')
                computador_venceu += 1
            elif computador == 'Tesoura':
                print(
                    f'\nVocê: {pedra_icon} x Computador: {tesou_icon}\n\n-- Pedra Quebra Tesoura --\n\nVocê Ganhou!')
                jogador_venceu += 1
            elif computador == 'Lagarto':
                print(
                    f'\nVocê: {pedra_icon} x Computador: {lagar_icon}\n\n-- Pedra Esmaga Lagarto --\n\nVocê Ganhou!')
                jogador_venceu += 1
            elif computador == 'Spock':
                print(
                    f'\nVocê: {pedra_icon} x Computador: {spock_icon}\n\n-- Spock Vaporiza Pedra --\n\nComputador Ganhou!')
                jogador_venceu += 1
            else:
                print(
                    f'\nVocê: {pedra_icon} x Computador: {pedra_icon}\n\n-- Pedra & Pedra --\n\nEmpate!')

            sleep(5)
            system('cls')

        elif jogador == 'Papel':
            system('cls')

            if computador == 'Pedra':
                print(
                    f'\nVocê: {papel_icon} x Computador: {pedra_icon}\n\n-- Papel Cobre Pedra --\n\nVocê ganhou!')
                jogador_venceu += 1
            elif computador == 'Tesoura':
                print(
                    f'\nVocê: {papel_icon} x Computador: {tesou_icon}\n\n-- Tesoura Corta Papel --\n\nComputador Ganhou!')
                computador_venceu += 1
            elif computador == 'Lagarto':
                print(
                    f'\nVocê: {papel_icon} x Computador: {lagar_icon}\n\n-- Lagarto Come Papel --\n\nComputador Ganhou!')
                computador_venceu += 1
            elif computador == 'Spock':
                print(
                    f'\nVocê: {papel_icon} x Computador: {spock_icon}\n\n-- Papel Refuta Spock --\n\nVocê Ganhou!')
                jogador_venceu += 1
            else:
                print(
                    f'\nVocê: {papel_icon} x Computador: {papel_icon}\n\n-- Papel & Pedra --\n\nEmpate!')

            sleep(5)
            system('cls')

        elif jogador == 'Tesoura':
            system('cls')

            if computador == 'Pedra':
                print(
                    f'\nVocê: {tesou_icon} x Computador: {pedra_icon}\n\n-- Pedra Quebra Tesoura --\n\nComputador Ganhou!')
                computador_venceu += 1
            elif computador == 'Papel':
                print(
                    f'\nVocê: {tesou_icon} x Computador: {papel_icon}\n\n-- Tesoura Corta Papel --\n\nVocê Ganhou!')
                jogador_venceu += 1
            elif computador == 'Lagarto':
                print(
                    f'\nVocê: {tesou_icon} x Computador: {lagar_icon}\n\n-- Tesoura Decapita Lagarto --\n\nVocê Ganhou!')
                jogador_venceu += 1
            elif computador == 'Spock':
                print(
                    f'\nVocê: {tesou_icon} x Computador: {spock_icon}\n\n-- Spock Esmaga Tesoura --\n\nComputador Ganhou!')
                computador_venceu += 1
            else:
                print(
                    f'\nVocê: {tesou_icon} x Computador: {tesou_icon}\n\n-- Tesoura & Tesoura --\n\nEmpate!')

            sleep(5)
            system('cls')

        elif jogador == 'Lagarto':
            system('cls')

            if computador == 'Pedra':
                print(
                    f'\nVocê: {lagar_icon} x Computador: {pedra_icon}\n\n-- Pedra Esmaga Lagarto --\n\nComputador Ganhou!')
                computador_venceu += 1
            elif computador == 'Papel':
                print(
                    f'\nVocê: {lagar_icon} x Computador: {papel_icon}\n\n-- Lagarto Come Papel --\n\nVocê Ganhou!')
                jogador_venceu += 1
            elif computador == 'Tesoura':
                print(
                    f'\nVocê: {lagar_icon} x Computador: {tesou_icon}\n\n-- Tesoura Decapita Lagarto --\n\nComputador Ganhou!')
                computador_venceu += 1
            elif computador == 'Spock':
                print(
                    f'\nVocê: {lagar_icon} x Computador: {spock_icon}\n\n-- Lagarto Envenena Spock --\n\nVocê Ganhou!')
                jogador_venceu += 1
            else:
                print(
                    f'\nVocê: {lagar_icon} x Computador: {lagar_icon}\n\n-- Lagarto & Lagarto --\n\nEmpate!')

            sleep(5)
            system('cls')

        else:
            system('cls')

            if computador == 'Pedra':
                print(
                    f'\nVocê: {spock_icon} x Computador: {pedra_icon}\n\n-- Spock Vaporiza Pedra --\n\nVocê Ganhou!')
                jogador_venceu += 1
            elif computador == 'Papel':
                print(
                    f'\nVocê: {spock_icon} x Computador: {papel_icon}\n\n-- Papel Refuta Spock --\n\nComputador Ganhou!')
                computador_venceu += 1
            elif computador == 'Tesoura':
                print(
                    f'\nVocê: {spock_icon} x Computador: {tesou_icon}\n\n-- Spock Esmaga Tesoura --\n\nVocê Ganhou!')
                jogador_venceu += 1
            elif computador == 'Lagarto':
                print(
                    f'\nVocê: {spock_icon} x Computador: {lagar_icon}\n\n-- Lagarto Envenena Spock --\n\nComputador Ganhou!')
                computador_venceu += 1
            else:
                print(
                    f'\nVocê: {spock_icon} x Computador: {spock_icon}\n\n-- Spock & Spock --\n\nEmpate!')

            sleep(5)
            system('cls')

    if jogador_venceu > computador_venceu:
        print(
            f'Você {jogad_icon} {jogador_venceu} X Computador {compu_icon} {computador_venceu}\n\nVocê venceu! Parabéns!')

    elif jogador_venceu < computador_venceu:
        print(
            f'Você {jogad_icon} {jogador_venceu} X Computador {compu_icon} {computador_venceu}\n\nComputador venceu! Que pena!')

    else:
        print(
            f'Você {jogad_icon} {jogador_venceu} X Computador {compu_icon} {computador_venceu}\n\nFoi empate!')

    continuar = input('\nDeseja continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        system('cls')
        break
