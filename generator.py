import dictionary
from decimal import Decimal

# формулы
# низшая теплота сгорания газа принятого состава Qн:

qn = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c6CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c6CO2))) / Decimal('1000000'))  # Мдж/м3

qn = round(qn, 2)
print(qn)

# Теоретически необхожимое для горения количество воздуха, м3/м3:

V0 = Decimal((Decimal('0.01') * (Decimal(dictionary.v1) * Decimal(dictionary.c7CH4) + Decimal(dictionary.v2) * Decimal(
    dictionary.c7CO2))))  # м3/м3:

V0 = round(V0, 2)
print(V0)