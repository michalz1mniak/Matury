with open('pi.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())

def czy_rosnaco_malejacy(ciag):
    if ciag[0] >= ciag[1]:
        return False
    zmiana = 0

    for i in range(1,len(ciag)-1):
        if zmiana == 0:
            if ciag[i] < ciag[i+1]:
                continue
            else: 
                zmiana = 1
                continue
        else:
            if ciag[i] > ciag[i+1]:
                continue
            else:
                return False
    if zmiana == 1:
        return True
    else: return False

najd = ''
poz = 0
for dl in range(4, 10000):
    czy = 0
    akt = ''
    for i in range(dl):
        akt+=dane[i]
    if czy_rosnaco_malejacy(akt) == True:
        najd = akt
        poz = 0
        continue
    for j in range(dl, len(dane)):
        akt  = akt[1:] + dane[j]
        if czy_rosnaco_malejacy(akt) == True:
            najd = akt
            poz = j-dl+1
            czy = 1
    if czy == 0:
        break
    print(dl)
print(najd,poz+1)


