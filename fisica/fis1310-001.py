
def calcDist(Vm, time):
    dist = Vm * time
    return dist

v = int(input("Insira a velocidade media em km/h: "))
v = 140/3.6
time = float(input("Insira o tempo em segundos: "))
deslocation = float(input("Insira o deslocamento em metros: "))

distance = calcDist(v, time)
trainSize = distance - deslocation

print(trainSize)