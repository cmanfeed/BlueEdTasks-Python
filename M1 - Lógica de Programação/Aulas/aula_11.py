'''
    Faça um programa que leia nome e média de um aluno, guardando
    também a situação em um dicionário. No final, mostre o conteúdo
    da estrutura na tela.
'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print()
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

'''
    1.    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
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
