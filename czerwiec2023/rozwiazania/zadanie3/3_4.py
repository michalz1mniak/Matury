with open('anagram.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())

def na_dec(liczba):
    suma = 0
    pot = len(liczba) - 1
    for cyfra in liczba:
        suma = suma + int(cyfra)*2**pot
        pot-=1
    return suma

def na_bin(liczba):
    wyn = ''
    while liczba>0:
        wyn = str(liczba%2) + wyn
        liczba = liczba//2
    return wyn
def suma_roznych_cyfr(liczba):
    liczba = str(liczba)
    unikalne = []
    for cyfra in liczba:
        if int(cyfra) not in unikalne:
            unikalne.append(int(cyfra))
    suma = 0
    for cyfra in unikalne:
        suma+=cyfra
    return suma


niemazero = 0
maxsumacyfr = 0

for liczba in dane:
    l = na_dec(liczba)
    if '0' not in str(l):
        niemazero+=1
    if suma_roznych_cyfr(l) > suma_roznych_cyfr(maxsumacyfr):
        maxsumacyfr = l
print(niemazero, maxsumacyfr)