class Conta:
    def __init__(self, titular='José', saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def __str__(self):
        if self.__saldo == 0:
            return f'''
            Titular : {self.__titular}
            '''
        else:
            return f'''
            Titular : {self.__titular}
            Saldo   : {self.__saldo}
            '''

    def depositar(self, valor):
        self.__saldo += valor
        return f'''
        {self.__titular} seu saldo atual é {self.__saldo}.
        '''

    def __pode_sacar(self, valor_saque):
        return self.__saldo < valor_saque

    def sacar(self, valor):
        if valor > 0:
            if self.__pode_sacar(valor):
                return f'{self.__titular} você não tem R$ {valor} para sacar.'
            else:
                self.__saldo -= valor
                return f'{self.__titular} você sacou R$ {valor}.'
        else:
            print('Você não pode sacar ZERO reais e números negativos.')

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        self.__titular = valor
