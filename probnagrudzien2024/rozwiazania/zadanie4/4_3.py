with open('prostokaty.txt') as p:
    wysokosci = []
    dane = []
    for i in p:
        dane.append(i.split())
        dane[-1][0] = int(dane[-1][0])
        dane[-1][1] = int(dane[-1][1])
        if dane[-1][0] not in wysokosci:
            wysokosci.append(dane[-1][0])

mx2 = 0
mx3 = 0
mx5 = 0

for wysokosc in wysokosci:
    szer = []
    for para in dane:
        if para[0] == wysokosc:
            szer.append(para[1])
    szer.sort(reverse=True)
    if len(szer)>=2:
        if szer[0] + szer[1]>mx2:
            mx2 = szer[0] + szer[1]
    if len(szer)>=3:
        if szer[0] + szer[1] + szer[2]>mx3:
            mx3 = szer[0] + szer[1] + szer[2]
    if len(szer)>=5:
        if szer[0] + szer[1] + szer[2] + szer[3] + szer[4]>mx5:
            mx5 = szer[0] + szer[1] + szer[2] + szer[3] + szer[4]


print(mx2,mx3,mx5)




    