with open('liczby.txt') as f:
    dane = []
    for i in f:
        dane.append(int(i.strip()))
        
cyfry = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
ciag = ''

for i in range(len(dane)):
    ciag += hex(dane[i])[2:]

for cyfra in cyfry:
    print(cyfra, ciag.count(cyfra))