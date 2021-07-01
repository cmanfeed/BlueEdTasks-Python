from conta import Conta

if __name__ == '__main__':

    banco = list()

    while True:
        conta = Conta(input('Digite o nome do titular: '),
                      int(input('Digite o saldo do titular: ')))
        
        banco.append(conta)

        flag = input('Deseja continuar? [S/N] ').strip().upper()
        if flag == 'N':
            break

print(banco[1].depositar(100))

for c in banco:
    print(c)