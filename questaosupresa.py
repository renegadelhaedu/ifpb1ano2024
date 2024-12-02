alunos = []

op = -2
while op != 0:
    print('\n--------------MENU-------------')
    print('1-inserir aluno')
    print('2-buscar aluno')
    print('0-sair')

    op = int(input('digite a opcao desejada'))
    if op == 1:
        nome = input('qual o nome do aluno').upper()
        alunos.append(nome)
    elif op == 2:
        nome_busca = input('digite o nome do aluno').upper()
        achei = False
        for nome in alunos:
            if nome_busca in nome:
                achei = True
                print('esse aluno está presente')

        if not achei:
            print('esse aluno faltou')

print('o programa encerrou')