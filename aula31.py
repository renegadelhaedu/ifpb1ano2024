
turmas = [['1 ano', 24], ['2 ano', 26], ['3 ano', 23]]

opcao = input('voce quer matricular um aluno ou desmatricular')

if opcao == 'matricular':
    nome_turma = input('qual turma vc deseja matricular')

    for turma in turmas:
        if nome_turma == turma[0]:
            turma[1] += 1

    print(turmas)




