op = -1
lista_alunos = []

while op != 0:
    print('\n\n-------MENU------')
    print('1-cadastre um aluno')
    print('2-coloque nota no aluno')
    print('3-exibir aprovados')
    print('4-Listar todos os alunos')

    op = int(input('digite a opcao desejada'))

    if op == 1:
        nome = input('digite o nome')
        cod = int(input('digite o código do aluno'))
        lista_alunos.append([nome, cod, 0])
    elif op == 2:
        achei = False
        cod_aluno = int(input('digite o código do aluno para inserir a nota'))
        for aluno in lista_alunos:
            if aluno[1] == cod_aluno:
                aluno[2] = float(input('digite sua nota'))
                print(lista_alunos)
                achei = True
        if not achei:
            print('código de aluno inexistente')

    elif op == 3:
        for aluno in lista_alunos:
            if aluno[2] >= 7:
                print('Nome:', aluno[0], '   nota:',aluno[2])

    elif op == 4:
        for aluno in lista_alunos:
            print('nome:', aluno[0], ' código:', aluno[1])
