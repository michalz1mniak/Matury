with open('slowa.txt') as plik:
    dane = []
    for i in plik:
        dane.append(i.strip())


def czy(slowo):
    kod_rot = ''
    for litera in slowo:
        kod = ord(litera)
        if kod + 13 <= 122:
            kod_rot += chr(kod+13)
        else:
            kod_rot += chr(97 + (12 - (122 - kod)))
    if kod_rot[::-1] == slowo: # [::-1] - odwrocenie slowa
        return True
    else: return False

licznik = 0
najd = ''
for s in dane:
    if czy(s):
        licznik+=1
        if len(s) > len(najd):
            najd = s
print(licznik, najd)
        
        