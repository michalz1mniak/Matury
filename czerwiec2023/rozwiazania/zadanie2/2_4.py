with open('slowa4.txt') as f:
    dane = []
    for i in f:
        dane.append(i.split())

def najm_sufiks(slowo):
    sufiksy = []
    for i in range(0,len(slowo)):
        sufiksy.append(slowo[i:])
    sufiksy.sort()
    return sufiksy[0]

for para in dane:
    print(najm_sufiks(para[1]))
