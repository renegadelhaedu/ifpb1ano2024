import minhas_funcoes as mf
import minhas_funcoes_adm as mfa

usuarios = [['Maria Alice', 'mary28', '10'], ['a', 'a', 'a']]
filmes = [['Harry Potter',3, 26, 0, 6] ,['Senhor dos Aneis',4, 28, 45, 8]]

op = 99
while op != 0:
    print('\n\n')
    print('---CINE LUX---')
    print('1- Cadastrar usuário')
    print('2- Fazer Login')
    print('0- Sair')

    op = int(input('digite a opção desejada: '))

    if op == 1:
        nome = input('digite seu nome')
        login = input('digite seu login')
        senha = input('digite sua senha')
        senha2 = input('confirme sua senha')

        mf.verificar_senha(senha, senha2, usuarios)
        print(usuarios)
    elif op == 2:
        login = input('digite seu login')
        senha = input('digite sua senha')

        admlogado = False
        usuariologado = False

        if login == 'mary28' and senha == '10':
            print('Login feito com sucesso!')
            admlogado = True

        else:
            for usuario in usuarios:
                if login == usuario[1] and senha == usuario[2]:
                    print('Login feito com sucesso!')
                    usuariologado = True


        if admlogado == True:
            op = -443
            while op != 3:
                op = mfa.menu_adm()

                if op == 1:
                    novo_filme = mf.inserir_filme()
                    filmes.append(novo_filme)
                    print('Filme cadastrado!')

                elif op == 2:
                    print(filmes)

        elif usuariologado == True:

            opc = 11
            while opc != 4:

                opc = mf.menu_usuario()

                if opc == 2:
                    for filme in filmes:
                        print(filme)

                elif opc == 3:
                    nome_filme = input('Qual filme deseja assistir?')
                    mf.comprar_ingresso(nome_filme, filmes)


        else:
            print('Voce não é nenhum dos dois.')