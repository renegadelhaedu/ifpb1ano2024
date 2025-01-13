sal = 1000
perc = 1.5
for ano in range(1996, 2026):
    sal = sal * (1 + perc/100)
    sal = round(sal, 2)
    perc = perc * 2
    print(ano, ' ganhou ', sal)