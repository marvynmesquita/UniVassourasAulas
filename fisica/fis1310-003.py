def calcTime(v, d):
    time = d / v
    return time

v1 = int(input("Insira a velocidade media em km/h nos primeiros momentos: "))
d1 = int(input("Insira a distância em km nos primeiros momentos: "))
v2 = int(input("Insira a velocidade media em km/h nos segundos momentos: "))
d2 = int(input("Insira a distância em km nos segundo momentos: "))
d3 = int(input("Insira a distância total em km: "))
time0 = int(input("Insira o tempo em minutos: "))
time0 = time0 / 60

time1 = calcTime(v1, d1)
time2 = calcTime(v2, d2)
d3 = d3 - (d2 + d1)
time3 = time0 - (time1 + time2)

print(f"A velocidade média no último trecho da viagem foi de {round(calcTime(time3, d3))} km/h")