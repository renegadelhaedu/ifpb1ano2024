#iniciar o uso do while para criar um programa de usuário

opcao = -2

while opcao != 0:
    print('---------MENU--------')
    print('1-Verificar se é sousense')
    print('2-Verificar se o aluno(a) mora em alojamento')
    print('0-Sair')

    opcao = int(input('digite a opcao desejada'))

    if opcao == 1:
        nome = input('digite seu nome')
        cidade = input('digite sua cidade')
        if cidade == 'Sousa' or cidade == 'sousa':
            print('Você é Sousense')


print('\nO PROGRAMA ENCERROU')