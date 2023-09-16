from math import *


# from itertools


def f_1(x):
    return x - x * x


def equ(a, b, c):
    D = b * b - 4 * a * c
    if D > 0:
        x1 = (- b + sqrt(D)) / (2 * a)
        x2 = (- b - sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = - b / (2 * a)
        return x
    return None


def l_3():
    a = input('Введите 3 числа через пробел: ').split()
    if len(a) == 3:
        a, b, c = float(a[0]), float(a[1]), float(a[2])
        return a, b, c
    else:
        return "Что-то пошло не так"


def l_4(x, y):
    return x * e ** 3 + tan(sqrt(abs(x - y)))


def l_5():
    p = [[0, 0], [0, 1], [1, 1], [4, 5], [7, 1], [-1, 3], [4, 4]]
    max = 0
    poi1 = [0, 0]
    poi2 = [0, 0]
    for i in range(0, len(p) - 1):
        a = sqrt((p[i][0] - p[i + 1][0]) ** 2 + (p[i][0] - p[i + 1][0]) ** 2)
        if a > max:
            max = a
            poi1 = [p[i][0], p[i][1]]
            poi2 = [p[i + 1][0], p[i + 1][1]]
    return max, poi1, poi2


def l_6():
    R, dot1, dot2 = input('Введите R и dot1, dot2: ').split()
    lenght1 =  sqrt((int(dot1)) ** 2 + (int(dot2)) ** 2)
    if lenght1 < int(R):
        return "Точка в окружности"
    elif lenght1 == R:
        return "Точка на окружности"
    else:
        return "Точка вне окружности"


print(l_6())
