qtde1 = 0
qtde2 = 0
qtde3 = 0
n = int(input('quantos eleitores existem?'))
qtde_votos = 0
while qtde_votos < n:
    qtde_votos += 1
    voto = int(input('voce deseja votar em qual candidato?'))
    if voto == 1:
        qtde1 = qtde1 + 1
    elif voto == 2:
        qtde2 += 1
    elif voto == 3:
        qtde3 += 1
    else:
        print('voto inválido')

if qtde1 > qtde2 and qtde1 > qtde3:
    print('o candidato 1 ganhou a eleiçao')
elif qtde2 > qtde1 and qtde2 > qtde3:
    print('o candidato 2 ganhou a eleiçao')
elif qtde3 > qtde2 and qtde3 > qtde1:
    print('o candidato 3 ganhou a eleiçao')