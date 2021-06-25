'''
    1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a
    soma desses três argumentos.
'''

import datetime


def sum_nums(n1, n2, n3):
    return n1 + n2 + n3


'''
    2. Faça um programa, com uma função que necessite de um argumento. A função retorna
    o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for
    negativo e ‘0’ se for 0.
'''


def check_positive(n):
    if n > 0:
        return 'Positivo'
    elif n < 0:
        return 'Negativo'
    else:
        return '0'


'''
    3. Faça um programa com uma função chamada somaImposto. A função possui dois
    parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
    porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o
    valor de custo para incluir o imposto sobre vendas.
'''


def soma_imposto(taxa_imposto, custo):
    return ((taxa_imposto/100) * custo) + custo


'''
    4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário
    é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha
    mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.
'''


def calc_salary(salary, hours):
    if hours >= 40:
        salary = (salary * 1.5) + salary

    return salary


'''
    5. Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha
    1, 68 e pese 75kg.
'''


def imc(height, weight):
    imc = weight / (height*height)

    if imc < 18.5:
        return 'Abaixo do Peso'
    elif 18.5 <= imc < 25:
        return 'Peso Normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    elif 30 <= imc < 35:
        return 'Obesidade Grau I'
    elif 35 <= imc < 40:
        return 'Obesidade Grau II'
    else:
        return 'Obesidade Grau III ou Mórbida'


'''
    6. Escreva uma função que, dado um número nota representando a nota de um estudante,
    converte o valor de nota para um conceito(A, B, C, D, E e F).
'''


def convert_to_grade(percentage):
    if percentage <= 10 and percentage >= 9.3:
        return 'A'
    elif 9.2 >= percentage >= 9:
        return 'A-'
    elif 8.9 >= percentage >= 8.8:
        return 'B+'
    elif 8.7 >= percentage >= 8.3:
        return 'B'
    elif 8.2 >= percentage >= 8:
        return 'B-'
    elif 7.9 >= percentage >= 7.8:
        return 'C+'
    elif 7.7 >= percentage >= 7.3:
        return 'C'
    elif 7.2 >= percentage >= 7:
        return 'C-'
    elif 6.9 >= percentage >= 6.8:
        return 'D+'
    elif 6.7 >= percentage >= 6:
        return 'D'
    else:
        return 'E / F'


'''
7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles
forem iguais, imprima que eles são iguais.
'''


def check_minor(n1, n2):
    if n1 < n2:
        print(f'O primeiro número é o menor: {n1}')
        return n1
    elif n1 > n2:
        print(f'O segundo número é o menor: {n2}')
        return n2
    else:
        print('São iguais!')
        return n1


'''
    DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no
    formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
    Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que
    Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro
    terá 29 dias.
'''


def construct_date(date_str):
    day, month, year = date_str.split('/')

    try:
        datetime.datetime(int(year), int(month), int(day))
    except:
        return 'Data não é valida!'

    month_names = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO',
                   'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

    return f'{day} de {month_names[int(month) - 1]} de {year}'
