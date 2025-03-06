with open('szachy.txt') as plik:
    plansze = []
    plansza = []
    for i in plik:
        if i != '\n':
            plansza.append(i.strip())
        else:
            plansze.append(plansza)
            plansza = []

            
bierki_biale = ['K', 'W', 'S', 'G', 'H', 'P']
bierki_czarne = ['k', 'w', 's', 'g', 'h', 'p']

def czy_rownowaga(p):
    czy = True
    for nr in range(6):
        ib = 0
        ic = 0
        for w in range(8):
            for k in range(8):
                if p[w][k] == bierki_biale[nr]:
                    ib+=1
                elif p[w][k] == bierki_czarne[nr]:
                    ic+=1
        if ic != ib:
            czy = False
            break
    return czy

def ile_bierek(p):
    ile = 0
    for w in range(8):
        for k in range(8):
            if p[w][k] != '.':
                ile+=1
    return ile

ilosc = 0
min_ilosc = 32
for plansza in plansze:
    if czy_rownowaga(plansza):
        ilosc+=1
        i = ile_bierek(plansza)
        if i < min_ilosc:
            min_ilosc = i
print(ilosc, min_ilosc)