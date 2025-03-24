with open('anagram.txt') as f:
    dane = []
    for i in f:
        liczba = i.strip()
        if len(liczba) == 8:
            dane.append(liczba)

def ilosc_jedynek(liczba):
    lj = 0
    lz = 0
    for cyfra in liczba:
        if cyfra == '1':
            lj+=1
    return lj

for liczba in dane:
    if ilosc_jedynek(liczba) == 4 or ilosc_jedynek(liczba) == 5:
        print(liczba)


