with open('liczby.txt') as f:
    dane = []
    for l in f:
        dane.append(l)

pierwszy_wiersz = dane[0].split()

maks_srednia = 0
maks_pierwsza = 0
maks_dl = 0

for dl in range(50,len(pierwszy_wiersz)):
    suma = 0
    for i in range(dl):
        suma+=int(pierwszy_wiersz[i])

    if suma/dl>maks_srednia:
        maks_srednia = suma/dl
        maks_pierwsza = pierwszy_wiersz[0]
        maks_dl = dl

    for i in range(dl,len(pierwszy_wiersz)):
        suma += int(pierwszy_wiersz[i])
        suma-= int(pierwszy_wiersz[i-dl])
        if suma/dl>maks_srednia:
            maks_srednia=suma/dl
            maks_pierwsza = pierwszy_wiersz[i-dl+1]
            maks_dl=dl

print(maks_srednia, maks_pierwsza, maks_dl)
    

