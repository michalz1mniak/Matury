with open('slowa.txt') as plik:
    dane = []
    for i in plik:
        dane.append(i.strip())
# sprawdzamy kazda litere w tym powtorzenia, da sie lepiej ale na potrzeby zadania wystaeczy
# mozna zrobic liste unikalnych liter w slowie z pomoca set() aby uniknac sprawdzania ewentualnych powtorzen
def czy(slowo):
    for litera in slowo: 
        ile = 0             
        for i in range(len(slowo)):
            if litera == slowo[i]:
                ile+=1
        if ile>len(slowo)/2:
            return True
    return False

for s in dane:
    if czy(s):
        print(s)