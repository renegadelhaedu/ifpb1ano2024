salarios = []
op = -99
while op != 0:
    print('-----MENU------')
    print('1-cadastrar salarios')
    print('2-somar todos os saláriosexibir todas as pessoas')
    print('3-calcular a media de salarios')
    print('0-sair')

    op = int(input('digite a opcao desejada '))

    if op ==1:
        novo_salario = float(input('digite seu salario'))
        salarios.append(novo_salario)
    elif op == 2:
        soma_salarios = sum(salarios)
        print('a soma dos salarios foi ', soma_salarios)
    elif op == 3:
        qtde = len(salarios)
        if qtde == 0:
            print('lista de salarios está vazia')
        else:
            media = sum(salarios) / len(salarios)
            print('a media foi ', media)

print('Programa encerrado com sucesso!')