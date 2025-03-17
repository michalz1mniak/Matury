with open('pi.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())
ile = 0
for i in range(len(dane)-1):
    para = int(dane[i] + dane[i+1])
    if para>90:
        ile+=1
print(ile)