with open('anagram.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())

def jaka(liczba):
    lj = 0
    lz = 0
    for cyfra in liczba:
        if cyfra == '1':
            lj+=1
        else:
            lz+=1
    if lj == lz:
        return 'z'
    elif abs(lj-lz) == 1:
        return 'pz'
    else:
        return None
    
lzr = 0
lpzr = 0
for l in dane:
    wyn = jaka(l)
    if wyn == 'z':
        lzr+=1
    elif wyn == 'pz':
        lpzr+=1
print(lzr,lpzr)
    