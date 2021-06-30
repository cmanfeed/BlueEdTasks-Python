class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nomePessoa = nome
        self.idadePessoa = idade
        self.pesoPessoa = peso

    # Se a pessoa tiver mais que 30 anos, as calorias de comer são em dobro
    def comer(self, calorias):
        if self.idadePessoa > 30:
            self.pesoPessoa = self.pesoPessoa + calorias * 2
        else:
            self.pesoPessoa = self.pesoPessoa + calorias

    # Se a pessoa tiver menos que 30 anos, as calorias de malhar são em dobro
    def malhar(self, calorias):
        if self.idadePessoa < 30:
            self.pesoPessoa = self.pesoPessoa - calorias * 2
        else:
            self.pesoPessoa = self.pesoPessoa - calorias

    def mostrarDados(self):
        return f'''
            Nome = {self.nomePessoa}
            Idade = {self.idadePessoa}
            Peso = {self.pesoPessoa}
        '''

'''
    Crie uma classe chamada Conta para simular as operações de uma conta corrente.
    Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar.
    Crie um objeto da classe Conta e teste os atributos e métodos implementados.​
    Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for
    maior que zero, caso contrário mostre a mensagem na tela:
            "Você não tem saldo suficiente para essa operação"
'''


class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo < 0 or valor > self.saldo:
            print('Você não tem saldo suficiente para essa operação.')
        else:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def mostrarDados(self):
        print(f'''
              Titular: {self.titular}
              Saldo : {self.saldo}
              ''')
