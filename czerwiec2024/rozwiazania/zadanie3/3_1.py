with open('slowa.txt') as plik:
    dane = []
    for i in plik:
        dane.append(i.strip())

def czy(slowo):
    for i in range(len(slowo)-2):
        if slowo[i] == 'k' and slowo[i+2] == 't':
            return True
    return False

licznik = 0
for s in dane:
    if czy(s):
        licznik+=1
print(licznik)

