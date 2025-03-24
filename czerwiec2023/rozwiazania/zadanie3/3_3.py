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
max_wart = 0
for i in range(len(dane)-1):
    wart = abs(na_dec(dane[i]) - na_dec(dane[i+1]))
    if wart>max_wart:
        max_wart = wart
print(na_bin(max_wart))