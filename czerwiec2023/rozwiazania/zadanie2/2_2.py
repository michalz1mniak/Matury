def czymniejszyn(slowo,k1,k2):
    i = k1 - 1
    j = k2 - 1
    while i<len(slowo) and j<len(slowo):
        if slowo[i] == slowo[j]:
            i+=1
            j+=1
        else:
            if slowo[i] < slowo[j]:
                return True
            else: 
                return False
    if j < len(slowo):
        return True
    else:
        return False





with open('slowa1.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())
    dane[2] = dane[2].split()

print(czymniejszyn(dane[1],int(dane[2][0]), int(dane[2][1])))

with open('slowa2.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())
    dane[2] = dane[2].split()

print(czymniejszyn(dane[1],int(dane[2][0]), int(dane[2][1])))

with open('slowa3.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())
    dane[2] = dane[2].split()

print(czymniejszyn(dane[1],int(dane[2][0]), int(dane[2][1])))
