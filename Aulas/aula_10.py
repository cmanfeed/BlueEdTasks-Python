# '''
#     #01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:

#     [1][2][3]
#     [4][5][6]
#     [7][8][9]

#     matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# '''

matriz = list()

for i in range(3):
    linha = list()

    for j in range(3):
        linha.append(int(input('Informe o valor: ')))

    matriz.append(linha)

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]}]', end='')
    print('')

# '''
#     #02 - Aprimore o desafio anterior, mostrando no final:
#     A) A soma de todos os valores pares digitados.
#     B) A soma dos valores da terceira coluna. 
#     C) O maior valor da segunda linha.
# '''

soma_pares = soma_terceira_coluna = maior_valor_segunda = 0

for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]

for i in range(3):
    soma_terceira_coluna += matriz[i][2]

for i in range(3):
    if matriz[1][i] > maior_valor_segunda:
        maior_valor_segunda = matriz[1][i]

print(f'''
Soma dos números pares          : {soma_pares}
Soma da terceira coluna         : {soma_terceira_coluna}
Maior valor da segunda coluna   : {maior_valor_segunda}
''')

# '''
#     03 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:
#         # Quantas pessoas foram cadastradas
#         # Mostre o maior peso
#         # Mostre o menor peso
# '''

pessoas = list()
pesos = list()

while True:
    pessoas.append(input('Informe o nome da pessoa: '))
    pesos.append(float(input('Informe o peso da pessoa: ')))

    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'''
Quantidade de pessoas cadastradas   : {len(pessoas)}
Maior peso cadastrado               : {max(pesos)}
Menor peso cadastrado               : {min(pesos)}
''')
