#funções é a forma como se define um bloco de código que pode ser
#chamado. o uso de funcoes facilita o reaproveitamento de código

#defini uma função
def exibir_mensagem():
    nome = input('digite seu nome')
    print('seja bem-vinda(o)', nome)

#a funçao abaixo possui um parâmetro de entrada
def calcular_idade(ano, nome):
    idade = 2025 - ano
    if nome == 'rene':
        idade = idade - 5
    print('o usuario ',nome, ' possui idade ', idade)

calcular_idade(2008, 'junior')
calcular_idade(1988, 'rene')
calcular_idade(2007, 'gabriel')
