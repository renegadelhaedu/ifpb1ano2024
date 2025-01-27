#lista é uma estrutura de dados que os organiza de forma sequencial
alunos = [['rene', 45], ['victor', 92], ['luiza', 89]]
idades = [15,16,16,15,16,15]

#adiciona na lista
idades.append(3)

#remove pelo índice do elemento
idades.pop(1)

#remove o item especificado na lista
idades.remove(16)

numero = int(input('digite o numero'))
if numero in idades:
    print('tem')
else:
    print('nao tem')

media = sum(idades) / len(idades)
print(media)