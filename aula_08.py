'''
    # Exercício 01 - Crie um programa que vai gerar cinco números
    aleatórios de 1 a 50 e coolocar em uma tupla. Depois disso, mostre a listagem
    de números gerados e também indique o menor e o maior número que estão
    na tupla. Sem utilizar repetições.
'''

from random import randint

tupla = (randint(1, 50), randint(1, 50), randint(1, 50),
         randint(1, 50), randint(1, 50))

print(f'''
Tupla Gerada: {tupla}
Maior número: {sorted(tupla)[-1]}
Menor número: {sorted(tupla)[0]}
''')

'''
    # Exercício 02 - Desenvolva um programa que leia quatro valores
    pelo teclado e guarde-os em uma tupla. No final, mostre:

    A) Quantas vezes apareceu o valor 9
    B) Em que posição foi digitado o primairo valor 3
'''

tupla = (int(input('Informe o 1º valor: ')),
         int(input('Informe o 2º valor: ')),
         int(input('Informe o 3º valor: ')),
         int(input('Informe o 4º valor: ')))

print(f'''
A) O número 9 apareceu {tupla.count(9)}x.
B) O primeiro valor 3 foi encontrado no index {tupla.index(3)}.
''')

'''
    # Exercício 03 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um
    programa que imprima as seguintes informações:
    a) tamanho da lista.
    b) maior valor da lista.
    c) menor valor da lista.
    d) soma de todos os elementos da lista.
    e) lista em ordem crescente.
    f) lista em ordem decrescente.
'''

l = [5, 7, 2, 9, 4, 1, 3]

print(f'''
Tamanho da lista                : {len(l)}
Maior valor da lista            : {max(l)}
Menor valor da lista            : {min(l)}
Soma dos elementos da lista     : {sum(l)}
''')

l.sort()
print(f'Lista em ordem crescente        : {l}')
l.reverse()
print(f'Lista em ordem decrescente      : {l}')

'''
    Desafio da noite:
    Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
    As perguntas são:
    
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
    
    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
    entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado
    como "Inocente".
'''

l = list()

p = ['Telefonou para a vítima? [S/N]  : ',
     'Esteve no local do crime? [S/N] : ',
     'Mora perto da vítima? [S/N]     : ',
     'Devia para a vítima? [S/N]      : ',
     'Já trabalhou com a vítima? [S/N]: ']

r = ['Inocente',
     'Suspeita',
     'Cúmplice',
     'Cúmplice',
     'Assassino']

for pergunta in p:
    l.append(int(input(pergunta).strip().upper()[0]
                 .replace('S', '1').replace('N', '0')))

print(f'O indíviduo é: {r[sum(l) - 1]}')
