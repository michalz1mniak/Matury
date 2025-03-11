with open('prostokaty.txt') as p:
    dane = []
    for i in p:
        dane.append(i.split())

mx = int(dane[0][0]) * int(dane[0][1])
mn = int(dane[0][0]) * int(dane[0][1])
for para in dane:
    pole = int(para[0]) * int(para[1])
    if pole>mx:
        mx = pole
    elif pole<mn:
        mn = pole
print(mx,mn)