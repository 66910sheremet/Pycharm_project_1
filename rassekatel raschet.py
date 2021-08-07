delta = 1
diamter = 6
height = 6
lagest = 0
a = []
while diamter <= 11:
    while height <= 23:
        KPD = 36.3091752883329 + (2.66579338833343 * diamter) + (0.613323721222232) - (0.118982154166671 * diamter ** 2) - (0.0281706407222229 * diamter * height) - (0.0102175696759261 * height ** 2)
        CO = 707.783333333346 - (62.9041666666692 * diamter) - (20.7408333333336 * height) + (2.48958333333345 * diamter ** 2) + (1.39388888888891 * diamter * height) + (0.302083333333337 * height ** 2)
        if CO < 360 and KPD > lagest:
            pred = lagest
            lagest = KPD
            height += delta
            a.append(KPD)
        elif KPD < lagest or CO > 360:
            height += delta
    height = 6
    diamter += delta
b = float(max(a))
for diamter in range(6,12):
    for height in range(6,24):
        if b == 36.3091752883329 + (2.66579338833343 * diamter) + (0.613323721222232) - (0.118982154166671 * diamter ** 2) - (0.0281706407222229 * diamter * height) - (0.0102175696759261 * height ** 2):
            print('диаметр =',diamter, 'высота =',height)