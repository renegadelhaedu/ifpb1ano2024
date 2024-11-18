sal_bruto = float(input('digite o seu salário'))
prestacao = float(input('digite o valor da prestacao'))

if prestacao > 0.3 * sal_bruto:
    print('sem emprestímo')
else:
    print('empréstimo OK')