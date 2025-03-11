with open('liczby.txt') as p:
    dane = []
    for l in p:
        dane.append(l.strip())

def procedura(liczba):
    mn = sorted(liczba)
    mn = mn[0] + mn[1] + mn[2] + mn[3]
    mx = sorted(liczba, reverse=True)
    mx = mx[0] + mx[1] + mx[2] + mx[3]
    mn = int(mn)
    mx = int(mx)

    return mx-mn

rowne = []
mniejsze = 0
wieksze = 0

for l in dane:
    wp = procedura(l)
    if wp > int(l):
        wieksze+=1
    elif wp < int(l):
        mniejsze+=1
    else:
        rowne.append(int(l))
print(mniejsze,wieksze,len(rowne),rowne)
    
