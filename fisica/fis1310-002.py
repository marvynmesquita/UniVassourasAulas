def calcVel(desloc, drops):
    vel = desloc / drops
    return vel

desloc = float(input("Insira o deslocamento em metros: "))
drops = int(input("Insira a quantidade de gotas por metro: "))
drops = drops/4

print(f'A velocidade média é de {calcVel(desloc, drops)} m/s.')