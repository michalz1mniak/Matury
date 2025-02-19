with open('odbiorcy.txt') as f:
    dane = []
    for i in f:
        dane.append(int(i.strip()))

ile = 0
for i in range(1,1025):
    if i not in dane:
        ile+=1
print(ile)
