notas = [200, 100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

def calTroco(troco):
    trocoFinal = []
    while troco > 0:
        for nota in notas:
            if nota <= troco:
                trocoFinal.append(nota)
                troco -= float(nota)
        if troco <= 1:
            for moeda in moedas:
                if moeda <= troco:
                    trocoFinal.append(moeda)
                    troco -= float(moeda)
    
    return trocoFinal


compra = float(input('Qual o valor total da compra? '))
pago = float(input('Qual o valor pago? '))

troco = pago - compra
print(f'O troco deve ser dado com {calTroco(troco)}')