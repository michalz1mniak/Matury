with open('bin.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())

def bloki(zapis):
    ile = 1
    for i in range(1,len(zapis)):
        if zapis[i] != zapis[i-1]:
            ile+=1
    return ile

odp = 0
for n in dane:
    if bloki(n) <= 2:
        odp+=1
print(odp)