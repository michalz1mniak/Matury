def potega(a,x,M):
    if x == 0:
        return 1 %M
    if x%2 == 0:
        y = potega(a,x//2,M) 
        return (x*x) %M      # mozemy bo (a*b) mod M = ((a mod M) * (b mod M)) mod M
    if x%2 == 1:
        y = potega(a,x//2,M)
        return (y*y*a) %M


