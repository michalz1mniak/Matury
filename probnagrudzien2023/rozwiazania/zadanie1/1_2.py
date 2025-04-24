with open('mecz.txt') as f:
    dane = []
    for i in f:
        dane.append(i.strip())
    dane = dane[0]

wygrane_a = 0
wygrane_b = 0

for r in dane:
    if r == "A":
        wygrane_a+=1
    else:
        wygrane_b+=1
    if wygrane_a >=1000 or wygrane_b>=1000:
        if abs(wygrane_a-wygrane_b) >=3:
            print(f'A: {wygrane_a} ,B: {wygrane_b}')
            break