with open('odbiorcy.txt') as f:
    dane = []
    for i in f:
        dane.append(int(i.strip()))

pakiety = []
for i in range(len(dane)):
    pakiety.append(dane[i])

max_w_komp = 0

for nr in range(1,len(dane)+1):
    temp = 0
    for gdzie in pakiety:
        if nr == gdzie:
            temp+=1
    if temp>max_w_komp:
        max_w_komp = temp
print(max_w_komp, end=' ')

for nr_rundy in range(2,9):
    for i in range(len(pakiety)):
        pakiety[i] = dane[pakiety[i]-1]
    if nr_rundy in [2,4,8]:
        max_w_komp = 0
        for nr in range(1,len(dane)+1):
            temp = 0
            for gdzie in pakiety:
                if nr == gdzie:
                    temp+=1
            if temp>max_w_komp:
                max_w_komp = temp
        print(max_w_komp, end=' ')



