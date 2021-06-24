# '''
#     Faça um programa que tenha uma função chamada voto() que vai receber
#     como parâmetro o ano de nascimento de uma pessoa, retornando um valor
#     literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓ-
#     RIO nas eleições:

#     # < 16 = NEGADO
#     # 16, 18 e mais que 70 = OPCIONAL
#     # As demais = OBRIGATÓRIO
# '''


def voto(ano_nascimento):
    from datetime import date

    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f'NEGADO'
    elif idade in [16, 18] or idade > 70:
        return f'OPCIONAL'
    else:
        return f'OBRIGATÓRIO'


ano_nascimento = int(input('Informe seu ano de nascimento: '))
print(f'Seu Voto é: {voto(ano_nascimento)}')

# '''
#     Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de
#     caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
# '''


def check_positive(n):
    if n > 0:
        return 'P'
    else:
        return 'N'


# '''
#     Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
#     1. A soma desses três parametros através de uma função.
#     2. Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.
# '''


def sum_numbers(n1, n2, n3):
    return n1 + n2 + n3


def mean_numbers(n1, n2, n3):
    return sum_numbers(n1, n2, n3)/3


def menu():
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))

    media = mean_numbers(n1, n2, n3)

    print(f'A média do aluno é {media:.2f}')


menu()
