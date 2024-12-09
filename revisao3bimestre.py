#desenvolva um algoritmo em python para ler os nomes e os salários
#dos funcionários de uma empresa. O programa deve ir lendo as
#informações até que o usuário digite a palavra "fim". ao final,
#exiba a quantidade de funcionários, a média salarial e o menor
#salário.
soma = 0
qtde = 0
menorSalario = 9999999999
maiorSalario = 0
nome = input('digite seu nome')
salario = float(input('digite seu salário'))
while nome != 'fim':
    soma = soma + salario
    qtde = qtde + 1

    if salario < menorSalario:
        menorSalario = salario #sobrescrever

    if salario > maiorSalario:
        maiorSalario = salario

    nome = input('digite seu nome')
    salario = float(input('digite seu salário'))

if qtde > 0:
    media = soma / qtde
    print('a quantidade foi ', qtde)
    print('a média foi ', media)
    print('o menor salário foi ', menorSalario)
    print('o maior salário foi ', maiorSalario)
else:
    print('não existem funcionários nessa empresa')

