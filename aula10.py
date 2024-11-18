saldo = float(input('digite o saldo médio'))

if(saldo >= 0 and saldo <= 500):
    cre = 0
elif saldo > 500 and saldo <= 1000:
    cre = saldo * 0.3
elif saldo > 1001 and saldo <= 3000:
    cre = saldo * 0.4
else:
    cre = saldo * 0.5

print('seu saldo é de ', saldo)
print('seu crédito será ', cre)