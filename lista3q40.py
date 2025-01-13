ind_mais_perigoso = 0
nome_mais_perigoso = ''
qtde_menos2000 = 0
soma_menos2000 = 0
for i in range(5):
    nome = input('digite o nome da cidade')
    numeroV = int(input('quantos numeros de veic tem em 1999'))
    acidentes = int(input('digite a quantidade de acidentes com vitimas'))

    if numeroV < 2000:
        soma_menos2000 += acidentes
        qtde_menos2000 += 1

    indice = acidentes / numeroV #menor melhor e maior pior

    if indice > ind_mais_perigoso:
        ind_mais_perigoso = indice
        nome_mais_perigoso = nome

print('a cidade mais perigosa é', nome_mais_perigoso)
media_cidade_menos2000 = soma_menos2000 / qtde_menos2000