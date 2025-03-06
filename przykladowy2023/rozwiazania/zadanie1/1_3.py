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

def czy_szachuje_bialy(p):
    for w in range(8):
        krol = False
        wieza = False
        for k in range(8):
            if p[w][k] == 'W':
                wieza = True
            elif p[w][k] == 'k':
                krol = True
            elif p[w][k] in bierki_biale or p[w][k] in bierki_czarne:
                wieza = False
                krol = False
            if krol and wieza:
                return True, w, k
    for k in range(8):
        krol = False
        wieza = False
        for w in range(8):
            if p[w][k] == 'W':
                wieza = True
            elif p[w][k] == 'k':
                krol = True
            elif p[w][k] in bierki_biale or p[w][k] in bierki_czarne:
                wieza = False
                krol = False
            if krol and wieza:
                return True, w, k
    return False
def czy_szachuje_czarny(p):
    for w in range(8):
        krol = False
        wieza = False
        for k in range(8):
            if p[w][k] == 'w':
                wieza = True
            elif p[w][k] == 'K':
                krol = True
            elif p[w][k] in bierki_biale or p[w][k] in bierki_czarne:
                wieza = False
                krol = False
            if krol and wieza:
                return True, w, k
    for k in range(8):
        krol = False
        wieza = False
        for w in range(8):
            if p[w][k] == 'w':
                wieza = True
            elif p[w][k] == 'K':
                krol = True
            elif p[w][k] in bierki_biale or p[w][k] in bierki_czarne:
                wieza = False
                krol = False
            if krol and wieza:
                return True, w, k
    return False

bialy = 0
czarny = 0

for plansza in plansze:
    if czy_szachuje_bialy(plansza):
        bialy+=1
    elif czy_szachuje_czarny(plansza):
        czarny+=1

print(bialy,czarny)
    
