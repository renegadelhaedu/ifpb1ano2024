nome = input('digite seu nome')
idade = int(input('digite sua idade'))

if idade >= 18:
    print(nome, 'voce vai para o show da xuxa')
else:
    anos = 18 - idade
    print(nome, 'quantidade de anos que falta para voce', anos)