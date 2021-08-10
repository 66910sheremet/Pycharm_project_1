def calc():
    delta = 0.01
    diamter = 6
    height = 6

    KPDtemp = 0
    COtemp = 0
    diameterT = 0
    heightT = 0
    while diamter < 12:
        while height < 24:
            KPD = 36.3091752883329 + (2.66579338833343 * diamter) + (0.613323721222232 * height) - (
                    0.118982154166671 * diamter ** 2) - \
                  (0.0281706407222229 * diamter * height) - (0.0102175696759261 * height ** 2)
            CO = 707.783333333346 - (62.9041666666692 * diamter) - (20.7408333333336 * height) + (
                    2.48958333333345 * diamter ** 2) + (
                         1.39388888888891 * diamter * height) + (0.302083333333337 * height ** 2)
            #print("KPD is " + str(KPD) + " CO is " + str(CO))
            if (CO < 360 and KPDtemp < KPD):
                KPDtemp = KPD
                COtemp = CO
                diameterT = diamter
                heightT = height
            height += delta
        height = 6
        diamter += delta
    return KPDtemp,diameterT,heightT

calc = calc()
print(calc[2])