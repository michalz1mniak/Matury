with open('liczby.txt') as f:
    dane = []
    for l in f:
        dane.append(l)

pierwszy_wiersz = dane[0].split()
drugi_wiersz = dane[1].split()
    
for liczba2 in drugi_wiersz:
    l = int(liczba2)
    for liczba1 in pierwszy_wiersz:
        if l%int(liczba1) == 0:
            l = l//int(liczba1)
    if l == 1:
        print(liczba2)

