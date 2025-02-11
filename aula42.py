#apenas listas, conjuntos e dicionários podem ser acessados dentro de uma funçao
#sendo declarada fora da função
def descobrir():
    alunos.append('caca')

alunos = ['toto']
descobrir()
print(alunos)

