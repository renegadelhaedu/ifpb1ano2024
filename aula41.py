#definiçao de uma função
def decidirEleitor(titulo):
    nome = input('digite seu nome')
    idade = int(input('digite sua idade'))
    msg = ''
    if idade >= 18:
        msg = 'voce é obrigado a votar ' + nome + ' Título de eleitor:' + titulo
    else:
        msg = 'voce ainda nao é obrigado a votar'

    return msg

tit = input('digite seu titulo de eleitor')

#chamar a função
saida = decidirEleitor(tit)
print(saida)