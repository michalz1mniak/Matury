with open('liczby.txt') as p:
    dane = []
    for l in p:
        dane.append(int(l.strip()))

def czy_kwadrat(liczba):
    i = 32
    while i*i<=liczba:
        if i*i == liczba:
            return True
        i+=1
    return False
ile = 0
c = True
for liczba in dane:
    if czy_kwadrat(liczba):
        ile+=1
        if c:
            print(liczba)
            c=False
print(ile)