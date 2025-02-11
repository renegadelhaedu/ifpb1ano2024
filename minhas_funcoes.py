def menu_usuario():
    print('\n\n')
    print('COMPRA DE INGRESSOS')
    print('2- Listar filmes')
    print('3- Comprar ingresso')
    print('4- Sair')

    return int(input('Digite sua opção: '))


def verificar_senha(senha, senha2, usuarios):
    while senha != senha2:
        senha = input('digite sua senha pois eram diferentes')
        senha2 = input('confirme sua senha novamente')

    usuarios.append([nome, login, senha])
    print('Usuário cadastrado com sucesso!')


def inserir_filme():
    film = input('Digite o nome do filme: ')
    s = int(input('Digite a quantidade de salas: '))
    m = float(input('Digite o preço do ingresso: '))
    q = int(input('Digite a quantidade de ingressos: '))
    h = int(input('Digite o horário do seu filme: '))

    # a palavra chave return é usada para a função retornar um valor
    return [film, s, m, q, h]


def comprar_ingresso(nome_filme, filmes):
    for filme in filmes:
        if nome_filme == filme[0]:
            if filme[3] <= 0:
                print('Sem ingressos disponíveis.')
            else:
                print('O valor do ingresso, é: ', filme[2])
                dindin = float(input('Digite o valor do pagamento: '))
                if dindin == filme[2]:
                    filme[3] -= 1
                    print('Ainda restam: ', filme[3], 'ingressos')
                    print('Seu ingresso foi comprado com sucesso!')
