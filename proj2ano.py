usuarios = []
op = -1
while op != 0:
    print('****** CINE SERTAO******')
    print('1-cadastrar usuário')
    print('2-fazer login')
    print('0-Sair do sistema')
    op = int(input('digite a opcao desejada'))
    if op == 1:
        nome = input('digite seu nome')
        login = input('digite seu login')
        senha = input('digite sua senha')

        usuarios.append([nome, login, senha])
        print(usuarios)
        print('---')