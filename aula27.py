usuarios = [['rene','rene88','123'], ['edivaldo','edi','222']]
filmes = []

op = 99
while op != 0:

    print('-MEU CINE SERTAO-')
    print('1-Cadastrar usuário')
    print('2-Fazer Login')
    print('0-sair')

    op = int(input('digite a opcao desejada'))

    if op == 1:
        nome = input('digite seu nome')
        login = input('digite seu login')
        senha = input('digite sua senha')
        senha2 = input('confirme sua senha')

        if senha == senha2:
            usuarios.append([nome, login, senha])
            print('usuário cadastrado com sucesso')
        else:
            print('voce digitou a senha incorreta')

    elif op == 2:
        login = input('digite seu login')
        senha = input('digite sua senha')
        clientelogado = False

        for usuario in usuarios:
            if login == usuario[1] and senha == usuario[2]:
                print('login feito com sucesso')
                clientelogado = True

        if clientelogado == True:
            print('MENU DE COMPRA DE INGRESSOS')
            print('1-comprar ingresso')
