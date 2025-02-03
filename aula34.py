professores = [['gustavo', 6.5],['rene', 1.5],['lairton', 3.5]]
achei_atleta = False

for professor in professores:
    if professor[1] > 10:
        print(professor[0], ' é um atleta ')
        achei_atleta = True

if achei_atleta == False:
    print('nenhum atleta foi encontrado')
