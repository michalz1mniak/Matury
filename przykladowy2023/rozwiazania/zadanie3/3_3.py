with open('liczby.txt') as p:
    dane = []
    for i in p:
        dane.append(i.split())

def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for dz in range(2, int(liczba**0.5)+1):
        if liczba%dz == 0:
            return False
    return True

ile = 0
for trojka in dane:
    if czy_pierwsza(int(trojka[0])):
        ile+=1
print(ile)