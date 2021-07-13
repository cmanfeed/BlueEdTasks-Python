'''
    Utilizando os conceitos de Orientação a Objetos(OO) vistos na aula
    anterior, crie um lançador de dados e moedas em que o usuário deve
    escolher o objeto a ser lançado. Não esqueça que os lançamentos são
    feitos de forma randômica.
'''

from random import randint, choice


class Lancador:
    def __init__(self, objeto):
        self.objeto = objeto

    def lancar(self):
        if self.objeto == 'dado':
            return randint(1, 7)
        elif self.objeto == 'moeda':
            return choice(['Cara', 'Coroa'])
        else:
            return 'Objeto não identificado'


'''
    #01 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
    programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
    quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
    dicionário, incluindo o total de gols feitos durante o campeonato.
    
    Vamos aprimorar o código: cadastro de jogador de futebol.py que foi
    desenvolvido no Code Lab da aula 14. Faça com que o seu código
    funcione para vários jogadores, incluindo um sistema de visualização de
    detalhes de aproveitamento de cada jogador.
'''


class Jogador():
    def __init__(self, nome, qtd_partidas, gols, qtd_gols):
        self.nome = nome
        self.qtd_partidas = qtd_partidas
        self.gols = gols
        self.qtd_gols = qtd_gols

    def mostrarStats(self):
        print(f'''
              Nome              : {self.nome}
              Qtd de Partidas   : {self.qtd_partidas}
              Gols              : {self.gols}
              Qtd Gols          : {self.qtd_gols}
              ''')


'''
    Crie uma classe que modele uma pessoa:
    a) Atributos: nome, idade, peso e altura.
    b) Métodos: envelhecer, engordar, emagrecer, crescer.
    Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela
    menor que 21 anos, ela deve crescer 0, 5 cm
'''


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.crescer(0.5)
        self.idade += 1

    def engordar(self, valor):
        self.peso += valor

    def emagrecer(self, valor):
        self.peso -= valor

    def crescer(self, valor):
        self.altura += valor

    def mostrarPessoa(self):
        print(f'''
              Nome      : {self.nome}
              Idade     : {self.idade}
              Peso      : {self.peso}
              Altura    : {self.altura}
              ''')
