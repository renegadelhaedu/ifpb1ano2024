dd = int(input('digite o dia'))
mm = int(input('digite o mes'))
aa = int(input('digite o ano'))

if dd > 0 and dd < 32 and mm > 0 and mm < 13 and aa > 0:
    print('Data Válida')
else:
    print('Data Inválida')
