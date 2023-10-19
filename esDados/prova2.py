n = int(input("Insira um numero inteiro: "))
a = 1
f = [1]

while a <= n:
    if a == 1:
        f.append(a)
        a = f[len(f)-1]+f[len(f)-2]
    elif a < n:
        a = f[len(f)-1]+f[len(f)-2]
        f.append(a)

print(f)