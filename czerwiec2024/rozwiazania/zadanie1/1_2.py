def Liczba_w_prawym_dolnym(w,k,n):
    dl = 0
    kopia_n = n

    while kopia_n > 0:
        dl+=1
        kopia_n = kopia_n // 2
    
    if w*k%dl == 0:
        ile = 1
    else: ile = dl - w*k%dl + 1

    for i in range(ile):
        x = n%2
        n=n//2
    
    return x


