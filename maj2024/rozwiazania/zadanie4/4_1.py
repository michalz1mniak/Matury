with open('liczby.txt') as f:
    dane = []
    for l in f:
        dane.append(l)
        
pierwszy_wiersz = dane[0].split()
drugi_wiersz = dane[1].split()

licznik = 0

for liczba1 in pierwszy_wiersz:
    for liczba2 in drugi_wiersz:
        if int(liczba2)%int(liczba1) == 0:
            licznik+=1
            break
print(licznik)


