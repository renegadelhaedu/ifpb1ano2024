#estrutura de repetição
#for
#faça um programa em python que leia o nome e a idade de 18 pessoas e
#e verifique quem é o mais velho

nome_exper = ''
idade_exper = 0
for i in range(4):
    nome = input('digite seu nome')
    idade = int(input('digite sua idade'))
    if idade > idade_exper:
        idade_exper = idade
        nome_exper = nome

print('o mais experiente é ', nome_exper)