with open('liczby.txt') as p:
    dane = []
    for i in p:
        dane.append(i.split())

def nwd(a,b):
    while b>0:
        r = a%b
        a = b
        b = r
    return a
ile = 0
for trojka in dane:
    if nwd(int(trojka[0]), int(trojka[1])) == 1:
        ile+=1
print(ile)
