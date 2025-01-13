#estrutura de repetição
#for para tabuada

qtde = 0
for i in range(106):
    salario = float(input('digite seu salario'))
    if salario >= 3000 and salario <= 3500:
        qtde = qtde + 1

print('a quanatidade de pessoas é ', qtde)

