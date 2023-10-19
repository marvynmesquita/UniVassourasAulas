c = float(input('Insira o valor aplicado: '))
i = float(input('Informe a taxa de juros anual: '))
n = int(input('Qual a quantidade de anos aplicado: '))

m = c * ((1 + i)**n)

print(f'O montante total será {m}')