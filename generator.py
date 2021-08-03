import dictionary

# формулы
# низшая теплота сгорания газа принятого состава Qн:

qn = (0.01 * (int(dictionary.v1) * int(dictionary.c6CH4) + int(dictionary.v2) * int(
    dictionary.c6CO2))) / 1000000  # Мдж/м3

# тут нужно дальше расписывать

print(qn)