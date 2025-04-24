with open('liczby.txt') as f:
    dane = []
    for i in f:
        dane.append(int(i.strip()))

def czypierwsza(liczba):
    if liczba < 2:
        return False
    for dz in range(2,int(liczba**0.5)+1):
        if liczba%dz == 0:
            return False
    return True

odp = 0
for liczba in dane:
    if czypierwsza(liczba-1) == True:
        odp+=1
print(odp)