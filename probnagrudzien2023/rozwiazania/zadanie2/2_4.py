with open('pary.txt') as f:
    dane = []
    for i in f:
        dane.append(i.split())
        dane[-1][0] = int(dane[-1][0])
        dane[-1][1] = int(dane[-1][1])

def czy(x,y):
    while y > x:
        if y//2 == x:
            return True
        y = y//2
    return False

for para in dane:
    if czy(para[0],para[1]):
        print(para)