alunos = [['rene', 45], ['victor', 92], ['luiza', 89]]

print(len(alunos))

soma = 0

for pessoa in alunos:
    soma = soma + pessoa[1]

#a funcao len determina a quantidade de itens dentro de uma lista
media = soma / len(alunos)

print(media)

