class Netflix:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Filme(Netflix):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\nDuração: {self.duracao}\nLikes: {self.likes}\n'


class Serie(Netflix):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\nDuração: {self.temporadas}\nLikes: {self.likes}\n'


vingadores = Filme('Guerra Infinita', 2018, 160)
print(vingadores)
