def funkcja(n):
    pozycja = 1
    while n>0:
        if n%2 == 1:
            print(pozycja)
        pozycja+=1
        n = n//2
    
funkcja(19)