from decimal import Decimal
from math import sin

import dictionary

# формулы
# 1. Низшая теплота сгорания газа принятого состава Qн:

qn = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c6CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c6CO2))) / Decimal('1000000'))  # Мдж/м3

qn = round(qn, 2)
print(qn)

# 2. Теоретически необходимое для горения количество воздуха, м3/м3:

V0 = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c7CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c7CO2))))  # м3/м3

V0 = round(V0, 2)
print(V0)

# 3. Абсолютная плотность газа принятого состава, кг/м3:

rg = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c4CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c4CO2))))  # кг/м3

rg = round(rg, 2)
print(rg)

# 4. Относительная плотность газа принятого состава:

S = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c5CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c5CO2))))

S = round(S, 2)
print(S)

# 5. Газовая постоянная газа принятого состава, Дж/(кг*К):

Rg = Decimal('831451') / (Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c1CH4) +
                                                      Decimal(dictionary.v2) * Decimal(
            dictionary.c1CO2)))))  # Дж/(кг*К)

Rg = round(Rg, 2)
print(Rg)

# 6. Показатель адиабаты газа принятого состава:

kg = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c3CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c3CO2))))

kg = round(kg, 2)
print(kg)

# 7. Изобраная теплоёмкость газа кДж/(кг * К):

Cp = (Decimal('1.695') + Decimal('0.001838') * (Decimal('273') + Decimal(dictionary.v6)) + Decimal('1960000') *
      ((Decimal(dictionary.v3) - Decimal('0.1')) / (Decimal('273') + Decimal(dictionary.v6)))) / Decimal('1000')

Cp = round(Cp, 2)
print(Cp)

# 8. Производительность газовой горелки при заданной мощности м3 / с:

Q1 = Decimal('3.6') * Decimal(Decimal(dictionary.v4) / Decimal('1000')) / Decimal(qn)

Q1 = round(Q1, 2)
print(Q1)

# 9. неоходимая суммарная площадь выходных отверстий головки горелки см2:

# А) Для отверстия круглого сечения:

Fod = Decimal(Decimal('0.01') * Decimal(dictionary.v14) * Decimal('3.14159') * Decimal(Decimal(dictionary.v8) * Decimal
('100')) * Decimal(Decimal(dictionary.v8) * Decimal('100'))) / Decimal('4')

Fod = round(Fod, 3)
print(Fod)

# Б) Для отверстия прямоугольного сечения:

Forc = Decimal('0.01') * Decimal(dictionary.v14) * Decimal(dictionary.v10) * Decimal(dictionary.v12) * Decimal('10000')

Forc = round(Forc, 3)
print(Forc)

# 10. Диаметр поперечного сечения головки горелки, мм:

# 1) Для круглых отверстий:

Dgol1 = (Decimal(Decimal('4') - Decimal(dictionary.v8))) / Decimal(sin(0.1))

Dgol1 = round(Dgol1, 3)
print(Dgol1)  # Диаметр головки должен быть от 3,5 до 100

# 1) Для прямоуголных отверстий:

Dgol2 = (Decimal(Decimal('4') - Decimal(dictionary.v10))) / Decimal(sin(0.1))

Dgol2 = round(Dgol2, 3)
print(Dgol2)  # Диаметр головки должен быть от 3,5 до 100

# 11. Скорость выхода газовоздушной смеси из огневых отверстий головки горелки м/с:

U_0 = (Decimal(Q1) * (Decimal('1') + Decimal(dictionary.v5) * Decimal(V0))) / Decimal(Fod)

U_0 = round(U_0, 2)
print(U_0)

# 12. Скорость истечения газа из сопла, м/с:

U_s = Decimal(dictionary.v15) * (
        ((Decimal('2') * Decimal(kg) * Decimal(Rg) * (Decimal('273') + Decimal(dictionary.v6))) /
         (Decimal(kg) - Decimal('1'))) * (
                Decimal('1') - (Decimal(dictionary.v7) / (Decimal(dictionary.v7) + Decimal(dictionary.v3))) **
                ((Decimal(kg) - Decimal('1')) / Decimal(kg)))) ** Decimal('0.5')

U_s = round(U_s, 2)
print(U_s)

# 13. Площадь сечения сопла см2:

Fc = (Decimal(Q1) / (Decimal('0.36') * Decimal(U_s))) * Decimal('10000')

Fc = round(Fc, 2)
print(Fc)


# 14. Оптимальные размеры теплового рассекателя
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
            print("KPD is " + str(KPD) + " CO is " + str(CO))
            if (CO < 360 and KPDtemp < KPD):
                KPDtemp = KPD
                COtemp = CO
                diameterT = diamter
                heightT = height
            height += delta
        height = 6
        diamter += delta
    return KPDtemp
