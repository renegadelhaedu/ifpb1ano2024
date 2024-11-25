#variável especial de lista e você inicia com um []
valores = ['bibi','perigosa']

nome = input('digite seu nome')
while nome != 'sair':
    #funcao para adicionar
    valores.append(nome)
    nome = input('digite seu nome')

print(valores)
