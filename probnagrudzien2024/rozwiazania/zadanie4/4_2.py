with open('prostokaty.txt') as p:
    dane = []
    for i in p:
        dane.append(i.split())
        dane[-1][0] = int(dane[-1][0])
        dane[-1][1] = int(dane[-1][1])

najd = 0
ostatni = 0
akt = 1

for i in range(1,len(dane)):
    if dane[i][0]<=dane[i-1][0] and dane[i][1]<=dane[i-1][1]:
        akt+=1
    else:
        if akt>najd:
            najd = akt
            ostatni = dane[i-1]
        akt = 1
print(najd,ostatni)

