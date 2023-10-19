import os;

class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

saldo = Conta(1320.00)

def extrato():
    return(f'Seu saldo atual é de {saldo.saldo:.2f}\n\n')

def saque(sacado, saldoAtual):
    if sacado > saldoAtual:
        return(f'Saldo indisponivel')
    else:
        saldo.saldo = saldoAtual-sacado
        return(f'Valor sacado. Seu saldo atual é de {saldo.saldo:.2f}\n\n')

def deposito(depositado, saldoAtual):
    saldo.saldo = saldoAtual+depositado
    return(f'Valor depositado. Seu saldo atual é de {saldo.saldo:.2f}\n\n')

def inicializar():
    print(f'O que deseja fazer?')
    print(f'Digite o numero da função desejada\n')
    print('1 - Mostrar saldo atual\n2 - Sacar dinheiro\n3 - Depositar dinheiro\n0 - Encerrar')
    opcao = int(input())
    if opcao == 1:
        os.system('clear')
        print(extrato())
        inicializar()
    if opcao == 2:
        os.system('clear')
        valor = float(input('Qual o valor desejado? '))
        os.system('clear')
        print(saque(valor, saldo.saldo))
        inicializar()
    if opcao == 3:
        os.system('clear')
        valor = float(input('Qual o valor desejado? '))
        os.system('clear')
        print(deposito(valor, saldo.saldo))
        inicializar()
    if opcao == 0:
        os.system('clear')
        print('Volte sempre!\n\n')
        exit()
    else:
        os.system('clear')
        print('Opção não encontrada\n\n')
        inicializar()


print(f'Bem-vindo ao PooBank!\n')
inicializar()