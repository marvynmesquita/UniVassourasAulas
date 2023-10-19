num = int(input('Insira um numero inteiro: '))
digitos = [int(i) for i in str(num)]
numInvertido = ''
for i in range(0,len(digitos)):
    j = len(digitos) - i
    numInvertido += str(digitos[j-1])

print(f'O número invertido é {numInvertido}')