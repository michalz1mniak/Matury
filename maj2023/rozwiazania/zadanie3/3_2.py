with open('pi.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())

fragmenty = []
for i in range(0,10):
    for j in range(0,10):
        fragmenty.append(str(i) + str(j))

najm = 9999
najmf = '00'
najw = 0
najwf = '00'

for fragment in fragmenty:
    ile = 0
    for i in range(len(dane)-1):
        para = dane[i] + dane[i+1]
        if para == fragment:
            ile+=1
    if ile < najm:
        najm = ile
        najmf = fragment
    if ile > najw:
        najw = ile
        najwf = fragment

print(najw,najwf)
print(najm,najmf)