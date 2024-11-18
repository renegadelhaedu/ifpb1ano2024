a = float(input('digite o lado'))
b = float(input('digite o lado'))
c = float(input('digite o lado'))

if a == 0:
    print('a equaçao nao é do segundo grau')
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('nao possui raizes reais')
    elif delta == 0:
        x1 = -b + delta ** (1/2)
        print('o valor de x1 é ', x1)
    else:
        x1 = -b + delta ** (1 / 2)
        x2 = -b - delta ** (1 / 2)
        print('o valor de x1 é', x1)
        print('o valor de x2 é', x2)
