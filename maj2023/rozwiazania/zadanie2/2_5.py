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

def zamiana_na_bin(liczba):
    wyn = ''
    while liczba>0:
        wyn = str(liczba%2) + wyn
        liczba = liczba // 2
    return wyn

def xor(a,b):
    while len(b) < len(a):
        b = '0' + b
    wyn = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            wyn += '1'
        else:
            wyn += '0'
    return wyn

for l in dane:
    x = l
    y = zamiana(x)//2
    y = zamiana_na_bin(y)

    print(xor(x,y))
    


