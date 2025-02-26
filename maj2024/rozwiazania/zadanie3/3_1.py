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
