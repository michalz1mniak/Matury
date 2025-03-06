with open('szachy.txt') as plik:
    plansze = []
    plansza = []
    for i in plik:
        if i != '\n':
            plansza.append(i.strip())
        else:
            plansze.append(plansza)
            plansza = []

def ile_pustych(p):
    ile = 0
    for k in range(8):
        czy_pusta = True
        for w in range(8):
            if p[w][k] != '.':
                czy_pusta = False
        if czy_pusta:
            ile+=1
    return ile



ile_z_pusta = 0
max_pustych = 0
for plansza in plansze:
    i = ile_pustych(plansza)
    if i>0:
        ile_z_pusta+=1
        if i>max_pustych:
            max_pustych = i
print(ile_z_pusta, max_pustych)
