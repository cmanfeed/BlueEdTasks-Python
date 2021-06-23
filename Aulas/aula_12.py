'''
    1. Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6,
    7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes
    aos quadrados desses números.
    {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}
'''

dics = dict()

for i in [1, 4, 5, 6, 7, 9]:
    dics[i] = i * i

print(dics)

'''
    2. Exercício Treino - Crie um dicionário em que suas chaves correspondem a números
    inteiros entre[1, 10] e cada valor associado é o número ao quadrado.
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
'''

dics = dict()

for i in range(1, 11):
    dics[i] = i * i

print(dics)

'''
    3. Faça um programa que leia nome e média de um aluno, guardando também a situação
    em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
    aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
    reprovado.
'''

aluno = dict()

aluno['name'] = input('Informe o nome do aluno: ')
aluno['mean'] = float(input('Informe a média do aluno: '))

if 7 <= aluno['mean']:
    aluno['result'] = 'Aprovado'
elif 5 <= aluno['mean'] < 7:
    aluno['result'] = 'Recuperação'
else:
    aluno['result'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} : {v}')

'''
    4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos(com idade) em 
    dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e 
    o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Considere que o 
    trabalhador deve contribuir por 35 anos para se aposentar.
'''

pessoa = dict()

pessoa['nome'] = input('Informe seu nome: ')
pessoa['anon'] = int(input('Informe seu ano de nascimento: '))
pessoa['ctps'] = int(input('Informe o número da carteira de trabalho: '))
pessoa['idad'] = 2021 - pessoa['anon']

if pessoa['ctps'] != 0:
    pessoa['ano_contratacao'] = int(input('Informe o ano de contratação: '))
    pessoa['salario'] = float(input('Informe seu salário: '))

    pessoa['anos_aposentadoria'] = 35 - (2021 - pessoa['ano_contratacao'])
else:
    pessoa['anos_aposentadoria'] = 35

print(f'''
{pessoa['nome']} você tem {pessoa['idad']} anos de idade.
Você levará cerca de {pessoa['anos_aposentadoria']} anos para se aposentar.
''')

'''
    5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
    guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
    lista. No final, mostre:
        A) Quantas pessoas estão cadastradas.
        B) A média da idade.
        C) Uma lista com as mulheres.
        D) Uma lista com as idades que estão acima da média.
        OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
        perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
'''

peoples = list()
womensl = list()
ab_mean = list()
age_sum = 0

while True:
    people = dict()
    people['nam'] = input('Informe o nome: ')

    while people['sex'] not in 'MF':
        people['sex'] = input(
            'Informe o sexo biológico [M/F]: ').strip().upper()[0]

    people['age'] = int(input('Informe a idade: '))

    age_sum += people['age']
    peoples.append(people)

    flag = input('Deseja continuar? [S/N]').strip().upper()[0]
    if flag == 'N':
        break

age_mean = age_sum/len(peoples)

for p in peoples:
    if p['sex'] == 'F':
        womensl.append(p)

    if p['age'] > age_mean:
        ab_mean.append(p)

print(f'''
Nº de pessoas cadastradas           : {len(peoples)}
Média da idade                      : {age_mean:.2f}
Mulheres                            : {womensl}
Pessoas com idade acima da média    : {ab_mean}
''')

'''
    6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve
    receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que
    calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios
    apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as
    situações dos 15 alunos de uma vez só.
'''

boletim = list()

for i in range(15):
    aluno = dict()
    notas = list()

    aluno['nome'] = input('Informe o nome do aluno: ')
    for i in range(5):
        notas.append(float(input(f'Informe o valor da {i+1}º nota: ')))
    aluno['notas'] = notas
    aluno['media'] = sum(aluno['notas'])/5

    if 7 <= aluno['media']:
        aluno['result'] = 'Aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['result'] = 'Recuperação'
    else:
        aluno['result'] = 'Reprovado'

    boletim.append(aluno)

for aluno in boletim:
    for k, v in aluno.items():
        print(f'{k} : {v}')
