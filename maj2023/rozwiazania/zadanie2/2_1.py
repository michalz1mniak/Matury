def ile_blokow(n):
    ib = 1
    poprzednia = n%2
    n = n//2
    while n>0:
        if n%2 != poprzednia:
            ib+=1
        poprzednia = n%2
        n = n//2
    return ib

