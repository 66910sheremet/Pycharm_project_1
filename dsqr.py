import math
B = -2
A = 0.38
C = 0.38
print('A ** 2 * x - B * x + C = 0')
discr = B ** 2 - 4 * A * C
print(discr)
if discr > 0:
    x1 = (-B + math.sqrt(discr)) / (2 * A)
    x2 = (-B - math.sqrt(discr)) / (2 * A)
    print('x1=', x1, 'x2=', x2)
elif discr == 0:
    x = -B / (2 * A)
    print(x)
else:
    print('Корней нет')
