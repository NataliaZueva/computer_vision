def calc(a, b, c):
    try:
        a, b, c = int(a), str(b), int(c)
    except ValueError:
        return 'Введено не число'
    else:
        match b:
            case '+':
                return a + c
            case '-':
                return a - c
            case '*':
                return a * c
            case '/':
                if c != 0:
                    return a / c
                else:
                    return "Не стоит делить нa ноль"
            case _:
                return "Введен не правильный оператор"

while True:
    a, b, c = input('num-operator-num: ').split()
    print(calc(a, b, c))