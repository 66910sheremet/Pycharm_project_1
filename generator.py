from decimal import Decimal
from math import sin
from math import exp

import dictionary

# формулы
# 1. Низшая теплота сгорания газа принятого состава Qн:

qn = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c6CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c6CO2))) / Decimal('1000000'))  # Мдж/м3

qn = round(qn, 2)
print('1',qn,'Низшая теплота сгорания газа принятого состава, Мдж/м3')

# 2. Теоретически необходимое для горения количество воздуха, м3/м3:

V0 = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c7CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c7CO2))))  # м3/м3

V0 = round(V0, 2)
print('2',V0, 'Теоретически необходимое для горения количество воздуха, м3/м3')

# 3. Абсолютная плотность газа принятого состава, кг/м3:

rg = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c4CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c4CO2))))  # кг/м3

rg = round(rg, 2)
print('3',rg, 'Абсолютная плотность газа принятого состава, кг/м3')

# 4. Относительная плотность газа принятого состава:

S = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c5CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c5CO2))))

S = round(S, 2)
print('4', S, 'Относительная плотность газа принятого состава')

# 5. Газовая постоянная газа принятого состава, Дж/(кг*К):

Rg = Decimal('831451') / (Decimal(dictionary.v1) * Decimal(dictionary.c1CH4) + Decimal(dictionary.v2) * Decimal(dictionary.c1CO2))  # Дж/(кг*К)

Rg = round(Rg, 2)
print('5',Rg, 'Газовая постоянная газа принятого состава, Дж/(кг*К)')

# 6. Показатель адиабаты газа принятого состава:

kg = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c3CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c3CO2))))

kg = round(kg, 2)
print('6',kg,'Показатель адиабаты газа принятого состава')

# 7. Изобраная теплоёмкость газа кДж/(кг * К):

Cp = (Decimal('1.695') + Decimal('0.001838') * (Decimal('273') + Decimal(dictionary.v6)) + Decimal('1960000') *
      ((Decimal(dictionary.v3) - Decimal('0.1')) / (Decimal('273') + Decimal(dictionary.v6)))) / Decimal('1000')

Cp = round(Cp, 2)
print('7',Cp, 'Изобраная теплоёмкость газа кДж/(кг * К)')

# 8. Производительность газовой горелки при заданной мощности м3 / с:

Q1 = Decimal('3.6') * Decimal(Decimal(dictionary.v4) / Decimal('1000')) / Decimal(qn)

Q1 = round(Q1, 2)
print('8',Q1,'Производительность газовой горелки при заданной мощности м3 / с')

# 9. неоходимая суммарная площадь выходных отверстий головки горелки см2:

# А) Для отверстия круглого сечения:

Fod = Decimal(Decimal('0.01') * Decimal(dictionary.v14) * Decimal('3.14159') * Decimal(Decimal(dictionary.v8)) * Decimal(Decimal(dictionary.v8))) / Decimal('4')

Fod = round(Fod, 7)
print('9.1',Fod,'неоходимая суммарная площадь выходных отверстий головки горелки см2 (для круглого сечения)')

# Б) Для отверстия прямоугольного сечения:

Forc = Decimal('0.01') * Decimal(dictionary.v14) * Decimal(dictionary.v10) * Decimal(dictionary.v12)

Forc = round(Forc, 7)
print('9.2',Forc,'неоходимая суммарная площадь выходных отверстий головки горелки см2 (для прямоуголного сечения)')

# 10. Диаметр поперечного сечения головки горелки, мм:

# 1) Для круглых отверстий:

Dgol1 = (Decimal(Decimal('4') - Decimal(dictionary.v8))) / Decimal(sin(0.1))

Dgol1 = round(Dgol1, 3)
print('10.1',Dgol1, 'Диаметр поперечного сечения головки горелки, мм (для круглых отверстий)' )  # Диаметр головки должен быть от 3,5 до 100

# 1) Для прямоуголных отверстий:

Dgol2 = (Decimal(Decimal('4') - Decimal(dictionary.v10))) / Decimal(sin(0.1))

Dgol2 = round(Dgol2, 3)
print('10.2',Dgol2, 'Диаметр поперечного сечения головки горелки, мм (для прямоуголных отверстий)')  # Диаметр головки должен быть от 3,5 до 100

# 11. Скорость выхода газовоздушной смеси из огневых отверстий головки горелки м/с:

U_0 = (Decimal(Q1) * (Decimal('1') + Decimal(dictionary.v5) * Decimal(V0))) / Decimal(Fod)

U_0 = round(U_0, 2)
print('11',U_0, 'Скорость выхода газовоздушной смеси из огневых отверстий головки горелки м/с')

# 12. Скорость истечения газа из сопла, м/с:

U_s = Decimal(dictionary.v16) * (
        ((Decimal('2') * Decimal(kg) * Decimal(Rg) * (Decimal('273') + Decimal(dictionary.v6))) /
         (Decimal(kg) - Decimal('1'))) * (
                Decimal('1') - (Decimal(dictionary.v7) / (Decimal(dictionary.v7) + Decimal(dictionary.v3))) **
                ((Decimal(kg) - Decimal('1')) / Decimal(kg)))) ** Decimal('0.5')

U_s = round(U_s, 2)
print('12', U_s, 'скорость истечения газа из сопла, м/с')

# 13. Площадь сечения сопла см2:

Fc = (Decimal(Q1) / (Decimal('0.36') * Decimal(U_s)))

Fc = round(Fc, 2)
print('13',Fc, 'Площадь сечения сопла см2')


# 14. Оптимальные размеры теплового рассекателя
def calc():
    delta = 0.01
    diamter = 6
    height = 6
    KPDtemp = 0
    COtemp = 0
    diamterT = 0
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
                diamterT = diamter
                heightT = height
            height += delta
        height = 6
        diamter += delta
    return KPDtemp,diamterT,heightT

calc = calc()


d_rass = calc[1]  # диаметр основания рассекателя
h_rass = calc[2]    # высота рассекателя
print('14.1',d_rass, 'диаметр основания рассекателя, мм')
print('14.2',h_rass, 'высота рассекателя, мм')


# 15. Площадь внутренней поверхности крышки, м2:

Ftepl = Decimal(0.000001) * Decimal(3.14159/4) * Decimal(Decimal(Dgol1) ** Decimal(2) - Decimal(d_rass) ** Decimal(2) + Decimal(2) * Decimal(d_rass) * Decimal((Decimal(h_rass) ** Decimal(2)) + (Decimal(d_rass) ** Decimal(2))/Decimal(4))**Decimal(0.5))

Ftepl = round(Ftepl, 10)
print('15',Ftepl, 'Площадь внутренней поверхности крышки, м2')

# 16. Массовый расход газовоздушной смеси, кг/с:

Gpot = Decimal(U_s) * Decimal(Fc) * Decimal(Decimal(rg) + Decimal(dictionary.v5) * Decimal(V0) * Decimal(dictionary.c1air))

Gpot = round(Gpot, 2)
print('16',Gpot, 'Массовый расход газовоздушной смеси, кг/с')

#17. Конечная температура газовоздушной смеси на выходе из огневых отверстий горелки, С:

t_k = Decimal(dictionary.v18) - Decimal(Decimal(dictionary.v18) - Decimal(dictionary.v6)) * Decimal(exp( - ((Decimal(Ftepl) * Decimal(dictionary.v19)) / (Decimal(Gpot) * Decimal(Cp)))))

t_k = round(t_k, 2)
print('17',t_k, 'Конечная температура газовоздушной смеси на выходе из огневых отверстий горелки, С:')

# 18. Коэффициент сопротивления отверстий головки горелки:

djeta = Decimal(Decimal(1) - Decimal(dictionary.v15) ** Decimal(2)) / (Decimal(dictionary.v15) ** Decimal(2))

djeta = round(djeta, 2)
print('18',djeta, 'Коэффициент сопротивления отверстий головки горелки')

# 19. Коэффициент потерь энергии в головке горелки:

K1 = Decimal(djeta) + Decimal(2) * ((Decimal(t_k) + Decimal(273))) / Decimal(273) - Decimal(1)

K1 = round(K1, 2)
print('19',K1, 'Коэффициент потерь энергии в головке горелки')

# 20. Оптимальное значение параметра горелки:

Fopt = (Decimal(dictionary.v17) / Decimal(K1)) ** Decimal(0.5)

Fopt = round(Fopt, 2)
print('20',Fopt, 'Оптимальное значение параметра горелки')

# 21. Коэффициент объемной эжекции:

us = Decimal(dictionary.v5) * Decimal(V0)

us = round(us, 2)
print('21',us, 'Коэффициент объемной эжекции')

# 22. Коэффициент массовой эжекции:

u = Decimal(dictionary.v5) * Decimal(V0) / Decimal(S)

u = round(u, 2)
print('22',u, 'Коэффициент массовой эжекции')

# Если А < 1, то горелка работает в неоптимальном режиме:
# 23. Параметр А:

A1 = (Decimal(K1) * (Decimal(1) + Decimal(u)) * (Decimal(1) + Decimal(us)) * Decimal(Fc) * Decimal(Fopt)) / Decimal(Fod)

A1 = round(A1, 2)
print('23',A1, 'Параметр А')

# 24. Наименьший корень квадратного уравнения:

def sqr():
    import math
    B = -2
    A = float(A1)
    C = A
    # print('A ** 2 * x - B * x + C = 0')
    discr = B ** 2 - 4 * A * C
    # print(discr)
    if discr > 0:
        x1 = (-B + math.sqrt(discr)) / (2 * A)
        x2 = (-B - math.sqrt(discr)) / (2 * A)
        return x1,x2
    elif discr == 0:
        x3 = -B / (2 * A)
        return x3
    else:
        return print('Корней нет')

sqr = sqr()

x = min(sqr)
x = round(x, 4)
print('24', 'x =', x )

# 25. Параметр смесителя при неоптимальном режиме:

F_1 = Decimal(x) * Decimal(Fopt)

F_1 = round(F_1, 2)
print('25',F_1, 'Параметр смесителя при неоптимальном режиме')

# 26. Площадь горловины смесителя, см2:

F_gor = Decimal(F_1) * Decimal(Fod)

F_gor = round(F_gor, 2)
print('26',F_gor, 'Площадь горловины смесителя, см2')

# 27. Диаметр горловины смесителя, см2:

dg = Decimal(10) * ((Decimal(4) * Decimal(F_gor)) / Decimal(3.14159)) ** Decimal(0.5)

dg = round(dg, 2)
print('27',dg, 'Диаметр горловины смесителя, см2')

# Если А = 1, то горелка работает в оптимальном режиме:
# 28. Площадь горловины смесителя, см2, если А = 1:

F_gor_opt = Decimal(Fopt) * Decimal(Fod)

F_gor_opt = round(F_gor_opt, 2)
print('28',F_gor_opt, 'Площадь горловины смесителя оптимальная см2')

# 29. Диаметр горловины смесителя, см2 если А = 1:

dg_opt = Decimal('10') * ((Decimal('4') * Decimal(F_gor_opt)) / Decimal('3.14159')) **Decimal('0.5')

dg_opt = round(dg_opt, 2)
print('29',dg_opt, 'Диаметр горловины смесителя оптимальный, см2')



