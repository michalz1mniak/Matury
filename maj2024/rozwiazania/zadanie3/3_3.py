with open('skrot2.txt') as p:
    dane = []
    for l in p:
        dane.append(int(l.strip()))

def nieparzysty_skrot(n):
    m = 0
    p = 1
    while n>0:
        cyfra = n%10
        n = n//10
        if cyfra%2 == 1:
            m += cyfra*p
            p = p*10
    return m

def nwd(a,b):
    while b!=0:
        r = a%b
        a = b
        b = r
    return a

for l in dane:
    ns = nieparzysty_skrot(l)
    if nwd(ns,l) == 7:
        print(l)