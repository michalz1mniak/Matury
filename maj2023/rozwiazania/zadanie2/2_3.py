with open('bin.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())


def zamiana(zapis):
    pot = len(zapis) - 1
    suma = 0
    for cyfra in zapis:
        suma = suma + 2**pot * int(cyfra)
        pot-=1
    return suma

mx = '0'
for z in dane:
    if zamiana(mx) < zamiana(z):
        mx = z
print(mx)