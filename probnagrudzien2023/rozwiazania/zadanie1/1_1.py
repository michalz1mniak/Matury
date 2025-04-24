with open('mecz.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())
    dane = dane[0]
ile = 0

for i in range(1,len(dane)):
    if dane[i]!=dane[i-1]:
        ile+=1
print(ile)