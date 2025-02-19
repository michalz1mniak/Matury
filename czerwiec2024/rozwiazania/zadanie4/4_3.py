with open('odbiorcy.txt') as f:
    dane = []
    for i in f:
        dane.append(int(i.strip()))

pakiety = []
for i in range(len(dane)):
    pakiety.append(dane[i])

koniec = True
odp = None
nr_rundy = 1

while koniec:
    nr_rundy+=1
    for i in range(len(pakiety)):
        pakiety[i] = dane[pakiety[i]-1]
    for i in range(len(pakiety)):
        if i+1 == pakiety[i]:
            odp = [nr_rundy, i+1]
            koniec = False
            break
print(odp)




