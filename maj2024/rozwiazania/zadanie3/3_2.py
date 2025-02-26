with open('skrot.txt') as p:
    dane = []
    for l in p:
        dane.append(int(l.strip()))

def czy_istnieje(liczba):
    while liczba>0:
        cyfra = liczba%10
        if cyfra % 2 == 1:
            return True
        liczba = liczba//10
    return False

ile = 0
naj = 0

for l in dane:
    if czy_istnieje(l) == False:
        ile+=1
        if l>naj:
            naj = l

print(ile,naj)