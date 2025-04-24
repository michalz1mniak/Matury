with open('mecz.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())
    dane = dane[0]
ilosc = 0
passa = 1
najd = 0
jaka = ''
akt = dane[0]
for i in range(1,len(dane)):
    if dane[i] == akt:
        passa+=1
    else:
        if passa >= 10:
            ilosc += 1
        if passa>najd:
            najd = passa
            jaka = akt
        passa = 1
        akt = dane[i]
print(ilosc, najd, akt)

