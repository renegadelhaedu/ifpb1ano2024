#obs: nao faça o que junior faz
namoradas_jr = []
continuar = 'sim'
while continuar == 'sim':
    nome = input('qual o nome da menina?')
    cidade = input('qual a cidade?')

    tem = False
    for menina in namoradas_jr:
        if menina[1] == cidade:
            tem = True
    if tem:
       print('voce já tem uma namorada nesta cidade.'
             ' Milena mandou vc tomar vergonha na cara')
    else:
        namoradas_jr.append([nome, cidade])

    continuar = input('voce deseja continuar? sim ou nao')