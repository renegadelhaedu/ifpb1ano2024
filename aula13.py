#estrutura de repetição while (enquanto)

soma = 0
qtde = 0
idade = int(input('digite sua idade'))
while idade > 0:
    qtde = qtde + 1
    soma = soma + idade
    idade = int(input('digite sua idade'))

print('a soma de idade foi ', soma)
media = soma / qtde
media = round(media, 2)
print('a média das idades foi ', media)