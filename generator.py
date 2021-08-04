import dictionary
from decimal import Decimal

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
    dictionary.c4CO2))))   # кг/м3

rg = round(rg, 2)
print(rg)


# 4. Относительная плотность газа принятого состава:

S = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c5CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c5CO2))))

S = round(S, 2)
print(S)


# 5. Газовая постоянная газа принятого состава, Дж/(кг*К):

Rg = Decimal('831451')/(Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c1CH4) +
    Decimal(dictionary.v2) * Decimal(dictionary.c1CO2)))))    #Дж/(кг*К)

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

# 10. Диаметр поперечного сечения головки горелки:
