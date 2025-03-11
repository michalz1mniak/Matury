with open('liczby.txt') as p:
    dane = []
    for l in p:
        dane.append(int(l.strip()))

def ile_dzielnikow(liczba):
    czynniki = []
    dz = 2
    while liczba>1:
        if liczba%dz == 0:
            liczba = liczba//dz
            if dz not in czynniki:
                czynniki.append(dz)
        else: dz+=1
    return len(czynniki)

for liczba in dane:
    if ile_dzielnikow(liczba)>=5:
        print(liczba)

