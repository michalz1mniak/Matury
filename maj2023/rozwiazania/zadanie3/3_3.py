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
odp = 0
for i in range(5,len(dane)):
    c = dane[i] + dane[i-1] + dane[i-2] + dane[i-3] + dane[i-4] + dane[i-5]
    if czy_rosnaco_malejacy(c):
        odp+=1
print(odp)