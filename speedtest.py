import time

start = time.time()


def calc():
    delta = 1
    diamter = 6
    height = 6
    kpdtemp1 = 0
    diamtert1 = 0
    heightt1 = 0
    while diamter < 12:
        while height < 24:
            kpd = 36.3091752883329 + (2.66579338833343 * diamter) + (0.613323721222232 * height) - (
                    0.118982154166671 * diamter ** 2) - \
                  (0.0281706407222229 * diamter * height) - (0.0102175696759261 * height ** 2)

            co = 707.783333333346 - (62.9041666666692 * diamter) - (20.7408333333336 * height) + (
                    2.48958333333345 * diamter ** 2) + (
                         1.39388888888891 * diamter * height) + (0.302083333333337 * height ** 2)
            # print("kpd is " + str(kpd) + " co is " + str(co))
            if kpdtemp1 < kpd and co < 360:
                kpdtemp1 = kpd
                diamtert1 = diamter
                heightt1 = height
            height += delta
        height = 6
        diamter += delta
    # return kpdtemp1, diamtert1, heightt1

    delta = 0.1
    diamter = diamtert1 - 1
    height = heightt1 - 1
    kpdtemp2 = 0
    diamtert2 = 0
    heightt2 = 0
    while diamter < diamtert1 + 1:
        while height < heightt1 + 1:
            kpd = 36.3091752883329 + (2.66579338833343 * diamter) + (0.613323721222232 * height) - (
                    0.118982154166671 * diamter ** 2) - \
                  (0.0281706407222229 * diamter * height) - (0.0102175696759261 * height ** 2)

            co = 707.783333333346 - (62.9041666666692 * diamter) - (20.7408333333336 * height) + (
                    2.48958333333345 * diamter ** 2) + (
                         1.39388888888891 * diamter * height) + (0.302083333333337 * height ** 2)
            if kpdtemp2 < kpd and co < 360:
                kpdtemp2 = kpd
                diamtert2 = diamter
                heightt2 = height
            height += delta
        height = heightt1 - 1
        diamter += delta

    delta = 0.01
    diamter = diamtert2 - 0.1
    height = heightt2 - 0.1
    kpdtemp3 = 0
    diamtert3 = 0
    heightt3 = 0
    while diamter < diamtert2 + 0.1:
        while height < heightt1 + 0.1:
            kpd = 36.3091752883329 + (2.66579338833343 * diamter) + (0.613323721222232 * height) - (
                    0.118982154166671 * diamter ** 2) - \
                  (0.0281706407222229 * diamter * height) - (0.0102175696759261 * height ** 2)

            co = 707.783333333346 - (62.9041666666692 * diamter) - (20.7408333333336 * height) + (
                    2.48958333333345 * diamter ** 2) + (
                         1.39388888888891 * diamter * height) + (0.302083333333337 * height ** 2)
            if kpdtemp3 < kpd and co < 360:
                kpdtemp3 = kpd
                diamtert3 = diamter
                heightt3 = height
            height += delta
        height = heightt2 - 0.1
        diamter += delta
    return kpdtemp3, diamtert3, heightt3














calc = calc()
print(calc)



end = time.time()
print(end - start)

