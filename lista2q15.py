#operadores lógicos
# and or

l1 = int(input('digite o lado'))
l2 = int(input('digite o lado'))
l3 = int(input('digite o lado'))


if l1 == l2 and l2 == l3:
    print('triangulo equilatero')
elif l1 != l2 and l2 != l3 and l1 != l3:
    print('triangulo escaleno')
else:
    print('triangulo isosceles')