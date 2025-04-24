with open('liczby.txt') as f:
    dane = []
    for i in f:
        dane.append(int(i.strip()))

def sito(liczba):
    s = [True]*(liczba+1)
    s[0] = False
    s[1] = False
    for i in range(2,liczba+1):
        if s[i] == True:
            for j in range(2*i, liczba+1, i):
                s[j] = False
    return s

zad_sito = sito(1000000)

def ile_rozkladow(liczba):
    l = 2
    p = liczba - 2
    ile = 0
    while l<=p:
        if zad_sito[l] and zad_sito[p]:
            ile+=1
        l = l+1
        p = p-1
    return ile

najw_liczba = 0
najw_rozkladow = 0
najm_liczba = 0
najm_rozkladow = 1000000

for liczba in dane:
    i = ile_rozkladow(liczba)
    if i < najm_rozkladow:
        najm_rozkladow = i
        najm_liczba = liczba
    if i > najw_rozkladow:
        najw_rozkladow = i
        najw_liczba = liczba
print(najm_liczba, najm_rozkladow)
print(najw_liczba, najw_rozkladow)

    
