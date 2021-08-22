import time

start = time.time()

def calc():
    delta = 0.01
    diamter = 6
    height = 6
    kpdtemp = 0
    diamtert = 0
    heightt = 0
    while diamter < 12:
        while height < 24:
            kpd = 36.3091752883329 + (2.66579338833343 * diamter) + (0.613323721222232 * height) - (
                    0.118982154166671 * diamter ** 2) - \
                  (0.0281706407222229 * diamter * height) - (0.0102175696759261 * height ** 2)

            co = 707.783333333346 - (62.9041666666692 * diamter) - (20.7408333333336 * height) + (
                    2.48958333333345 * diamter ** 2) + (
                         1.39388888888891 * diamter * height) + (0.302083333333337 * height ** 2)
            # print("kpd is " + str(kpd) + " co is " + str(co))
            if kpdtemp < kpd and co < 360:
                kpdtemp = kpd
                diamtert = diamter
                heightt = height
            height += delta
        height = 6
        diamter += delta
    return kpdtemp, diamtert, heightt


calc = calc()
print(calc)

end = time.time()
print(end - start)