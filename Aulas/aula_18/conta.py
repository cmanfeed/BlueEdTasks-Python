class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        if self.saldo == 0:
            return f'''
            Titular : {self.titular}
            '''
        else:
            return f'''
            Titular : {self.titular}
            Saldo   : {self.saldo}
            '''

    def depositar(self, valor):
        self.saldo += valor
        return f'''
        {self.titular} seu saldo atual é {self.saldo}.
        '''

    def sacar(self, valor):
        if self.saldo <= 0:
            return 'O Saldo é Insuficiente'
        else:
            self.saldo -= valor
            return f'Saque realizado! Saldo atual: {self.saldo} '
