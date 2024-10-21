#desenvolva um programa para verificar se o dobro da idade
#de um aluno (leia a idade) é maior que 35

idade = int(input('digite sua idade'))
dobro = idade * 2
if dobro > 35:
    print('permitido')
else:
    print('nao permitido')
