with open('liczby.txt') as p:
    dane = []
    for i in p:
        dane.append(i.split())


def potega(p,w,m):
    if w == 0:
        return 1 %m
    if w%2 == 0:
        x = potega(p,w//2,m) 
        return (x*x) %m      # mozemy bo (a*b) mod M = ((a mod M) * (b mod M)) mod M
    if w%2 == 1:
        x = potega(p,w//2,m)
        return (x*x*p) %m
    
def czy(m,a,b):
    for x in range(0,m):
        if potega(a,x,m) == b:
            return True
    return False
ile = 0
i = 1
for trojka in dane:
    print(i)
    i+=1
    if czy(int(trojka[0]), int(trojka[1]), int(trojka[2])):
           ile+=1
    
print(ile)