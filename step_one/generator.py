import logging
import time
from decimal import Decimal
from math import exp
from math import sin

from step_one import dictionary

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

start = time.time()

# формулы
# 1. Низшая теплота сгорания газа принятого состава Qн:

qn = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c6CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c6CO2))) / Decimal('1000000'))  # Мдж/м3

qn = round(qn, 2)
logger.info('Низшая теплота сгорания газа принятого состава, %s Мдж/м3', qn)

# 2. Теоретически необходимое для горения количество воздуха, м3/м3:

V0 = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c7CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c7CO2))))  # м3/м3

V0 = round(V0, 2)
logger.info('Теоретически необходимое для горения количество воздуха, %s м3/м3', V0)

# 3. Абсолютная плотность газа принятого состава, кг/м3:

rg = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c4CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c4CO2))))  # кг/м3

rg = round(rg, 2)
logger.info('Абсолютная плотность газа принятого состава, %s кг/м3', rg)

# 4. Относительная плотность газа принятого состава:

S = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c5CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c5CO2))))

S = round(S, 2)
logger.info('Относительная плотность газа принятого состава %s', S)

# 5. Газовая постоянная газа принятого состава, Дж/(кг*К):

Rg = Decimal('831451') / (Decimal(dictionary.v1) * Decimal(dictionary.c1CH4) + Decimal(dictionary.v2) *
                          Decimal(dictionary.c1CO2))  # Дж/(кг*К)

Rg = round(Rg, 2)
logger.info('Газовая постоянная газа принятого состава, %s Дж/(кг*К)', Rg)

# 6. Показатель адиабаты газа принятого состава:

kg = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c3CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c3CO2))))

kg = round(kg, 2)
logger.info('Показатель адиабаты газа принятого состава %s', kg)

# 7. Изобраная теплоёмкость газа кДж/(кг * К):

Cp = (Decimal('1.695') + Decimal('0.001838') * (Decimal('273') + Decimal(dictionary.v6)) + Decimal('1960000') *
      ((Decimal(dictionary.v3) - Decimal('0.1')) / (Decimal('273') + Decimal(dictionary.v6)))) ** 3

Cp = round(Cp, 2)
logger.info('Изобраная теплоёмкость газа %s кДж/(кг * К)', Cp)

# 8. Производительность газовой горелки при заданной мощности м3 / с:

Q1 = Decimal('3.6') * Decimal(Decimal(dictionary.v4) / Decimal('1000')) / Decimal(qn)

Q1 = round(Q1, 2)
logger.info('Производительность газовой горелки при заданной мощности %s м3 / с', Q1)

# 9. неоходимая суммарная площадь выходных отверстий головки горелки см2:

# А) Для отверстия круглого сечения:

Fod = Decimal(Decimal('0.01') * Decimal(dictionary.v14) * Decimal('3.14159') * Decimal(Decimal(dictionary.v8)) *
              Decimal(Decimal(dictionary.v8))) / Decimal('4')

Fod = round(Fod, 7)
logger.info('неоходимая суммарная площадь выходных отверстий головки горелки %s см2 (для круглого сечения)', Fod)

# Б) Для отверстия прямоугольного сечения:

Forc = Decimal('0.01') * Decimal(dictionary.v14) * Decimal(dictionary.v10) * Decimal(dictionary.v12)

Forc = round(Forc, 7)
logger.info('неоходимая сумм. площадь выходных отверстий головки горелки %s см2 (для прямоуголного сечения)', Forc)

# 10. Диаметр поперечного сечения головки горелки, мм:

# 1) Для круглых отверстий:

Dgol1 = (Decimal(Decimal('4') - Decimal(dictionary.v8))) * Decimal(dictionary.v8) / Decimal(sin(0.1))

Dgol1 = round(Dgol1, 3)
logger.info('Диаметр поперечного сечения головки горелки, %s мм (для круглых отверстий)', Dgol1)
# Диаметр головки должен быть от 3,5 до 100

# 1) Для прямоуголных отверстий:

Dgol2 = (Decimal(Decimal('4') - Decimal(dictionary.v10))) * Decimal(dictionary.v8) / Decimal(sin(0.1))

Dgol2 = round(Dgol2, 3)
logger.info('Диаметр поперечного сечения головки горелки, %s мм (для прямоуголных отверстий)', Dgol2)
# Диаметр головки должен быть от 3,5 до 100

# 11. Скорость выхода газовоздушной смеси из огневых отверстий головки горелки м/с:

U_0 = (Decimal(Q1) * (Decimal('1') + Decimal(dictionary.v5) * Decimal(V0))) / Decimal(Fod)

U_0 = round(U_0, 2)
logger.info('Скорость выхода газовоздушной смеси из огневых отверстий головки горелки %s м/с', U_0)

# 12. Скорость истечения газа из сопла, м/с:

U_s = Decimal(dictionary.v16) * (
        ((Decimal('2') * Decimal(kg) * Decimal(Rg) * (Decimal('273') + Decimal(dictionary.v6))) /
         (Decimal(kg) - Decimal('1'))) * (
                Decimal('1') - (Decimal(dictionary.v7) / (Decimal(dictionary.v7) + Decimal(dictionary.v3))) **
                ((Decimal(kg) - Decimal('1')) / Decimal(kg)))) ** Decimal('0.5')

U_s = round(U_s, 2)
logger.info('скорость истечения газа из сопла, %s м/с', U_s)

# 13. Площадь сечения сопла см2:

Fc = (Decimal(Q1) / (Decimal('0.36') * Decimal(U_s)))

Fc = round(Fc, 2)
logger.info('Площадь сечения сопла %s см2', Fc)

# 14. Диаметр сечения сопла, мм:

d_c = Decimal(1000) * ((Decimal(4) * Decimal(Q1)) / (Decimal(3600) * Decimal(3.14159) * Decimal(U_s)))

d_c = round(d_c, 4)
logger.info('Диаметр сечения сопла, %s мм', d_c)


# 15. Оптимальные размеры теплового рассекателя
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
            # logger.info("kpd is " + str(kpd) + " co is " + str(co))
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

d_rass = calc[1]  # диаметр основания рассекателя
h_rass = calc[2]  # высота рассекателя
logger.info('диаметр основания рассекателя, %s мм', d_rass)
logger.info('высота рассекателя, %s мм', h_rass)

# 16. Площадь внутренней поверхности крышки, м2:

Ftepl = Decimal(0.000001) * Decimal(3.14159 / 4) * \
        Decimal(Decimal(Dgol1) ** Decimal(2) - Decimal(d_rass) ** Decimal(2) + Decimal(2) * Decimal(d_rass) *
                Decimal((Decimal(h_rass) ** Decimal(2)) + (Decimal(d_rass) ** Decimal(2)) / Decimal(4)) ** Decimal(0.5))

Ftepl = round(Ftepl, 10)
logger.info('Площадь внутренней поверхности крышки, %s м2', Ftepl)

# 17. Массовый расход газовоздушной смеси, кг/с:

Gpot = Decimal(U_s) * Decimal(Fc) * Decimal(Decimal(rg) + Decimal(dictionary.v5) * Decimal(V0) *
                                            Decimal(dictionary.c1air))

Gpot = round(Gpot, 2)
logger.info('Массовый расход газовоздушной смеси, %s кг/с', Gpot)

# 18. Конечная температура газовоздушной смеси на выходе из огневых отверстий горелки, С:

t_k = Decimal(dictionary.v18) - Decimal(Decimal(dictionary.v18) - Decimal(dictionary.v6)) * \
      Decimal(exp(- ((Decimal(Ftepl) * Decimal(dictionary.v19)) / (Decimal(Gpot) * Decimal(Cp)))))

t_k = round(t_k, 2)
logger.info('Конечная температура газовоздушной смеси на выходе из огневых отверстий горелки, С: %s', t_k)

# 19. Коэффициент сопротивления отверстий головки горелки:

djeta = Decimal(Decimal(1) - Decimal(dictionary.v15) ** Decimal(2)) / (Decimal(dictionary.v15) ** Decimal(2))

djeta = round(djeta, 2)
logger.info('Коэффициент сопротивления отверстий головки горелки %s', djeta)

# 20. Коэффициент потерь энергии в головке горелки:

K1 = Decimal(djeta) + Decimal(2) * (Decimal(t_k) + Decimal(273)) / Decimal(273) - Decimal(1)

K1 = round(K1, 2)
logger.info('Коэффициент потерь энергии в головке горелки %s', K1)

# 21. Оптимальное значение параметра горелки:

Fopt = (Decimal(dictionary.v17) / Decimal(K1)) ** Decimal(0.5)

Fopt = round(Fopt, 2)
logger.info('Оптимальное значение параметра горелки %s', Fopt)

# 22. Коэффициент объемной эжекции:

us = Decimal(dictionary.v5) * Decimal(V0)

us = round(us, 2)
logger.info('Коэффициент объемной эжекции %s', us)

# 23. Коэффициент массовой эжекции:

u = Decimal(dictionary.v5) * Decimal(V0) / Decimal(S)

u = round(u, 2)
logger.info('Коэффициент массовой эжекции %s', u)

# Если А < 1, то горелка работает в неоптимальном режиме:
# 24. Параметр А:

A1 = (Decimal(K1) * (Decimal(1) + Decimal(u)) * (Decimal(1) + Decimal(us)) * Decimal(Fc) * Decimal(Fopt)) / Decimal(Fod)

A1 = round(A1, 2)
logger.info('Параметр А %s', A1)


# 25. Наименьший корень квадратного уравнения:


def sqr():
    import math
    b = -2
    a = float(A1)
    c = a
    # logger.info('a ** 2 * x - b * x + c = 0')
    discr = b ** 2 - 4 * a * c
    # logger.info(discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr == 0:
        x3 = -b / (2 * a)
        return x3
    else:
        return logger.info('Корней нет')


sqr = sqr()

x = min(sqr)
x = round(x, 4)
logger.info('x = %s', x)

# 26. Параметр смесителя при неоптимальном режиме:

F_1 = Decimal(x) * Decimal(Fopt)

F_1 = round(F_1, 2)
logger.info('Параметр смесителя при неоптимальном режиме %s', F_1)

# 27. Площадь горловины смесителя, см2:

F_gor = Decimal(F_1) * Decimal(Fod)

F_gor = round(F_gor, 2)
logger.info('Площадь горловины смесителя, %s см2', F_gor)

# 28. Диаметр горловины смесителя, см2:

dg = Decimal(10) * ((Decimal(4) * Decimal(F_gor)) / Decimal(3.14159)) ** Decimal(0.5)

dg = round(dg, 2)
logger.info('Диаметр горловины смесителя, %s см2', dg)

# Если А = 1, то горелка работает в оптимальном режиме:
# 29. Площадь горловины смесителя, см2, если А = 1:

F_gor_opt = Decimal(Fopt) * Decimal(Fod)

F_gor_opt = round(F_gor_opt, 2)
logger.info('Площадь горловины смесителя оптимальная %s см2', F_gor_opt)

# 30. Диаметр горловины смесителя, см2 если А = 1:

dg_opt = Decimal('10') * ((Decimal('4') * Decimal(F_gor_opt)) / Decimal('3.14159')) ** Decimal('0.5')

dg_opt = round(dg_opt, 2)
logger.info('Диаметр горловины смесителя оптимальный, %s см2', dg_opt)

end = time.time()
logger.info(end - start)
