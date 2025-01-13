#estrutura de repetição for:
#1-realizar repetições com intervalo definido pela função range
#2-percorrer/iterar uma lista
# desenvolva um algoritmo em python que leia o nome de 4 alunos
# e os armazene dentro de uma lista. Após a leitura dos nomes,
# percorra a lista verificando se o querido aluno junior (o terror do if)
# veio para a aula. Informe ao final com uma mensagem em caso afirmativo e negativo

minha_lista = []

for popo in range(4):
    nome = input('digite seu nome').upper() #transforma tudo em maiúsculo
    minha_lista.append(nome) #adiciona dentro da lista

jr_veio = False
for nome_aluno in minha_lista:
    if nome_aluno == 'JUNIOR':
        jr_veio = True

print(minha_lista)
print('afinal, junior veio ou nao?')
if jr_veio == True:
    print('ele veio hoje.. oba, que ótimo!')
else:
    print('obrigado Deus')
