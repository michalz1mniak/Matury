with open('liczby.txt') as f:
    dane = []
    for l in f:
        dane.append(l)
        
pierwszy_wiersz = dane[0].split()
drugi_wiersz = dane[1].split()

for i in range(len(pierwszy_wiersz)):
    pierwszy_wiersz[i] = int(pierwszy_wiersz[i])

pierwszy_wiersz.sort(reverse=True)
print(pierwszy_wiersz[100])