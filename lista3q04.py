pop_a = 80000
pop_b = 200000
qtde_anos = 0
while pop_a < pop_b:
    pop_a = pop_a * (1 + 3/100) #aumentei por ano 3%
    pop_b = pop_b * (1 + 1.5/100) #aumentei por ano 1.5%
    qtde_anos = qtde_anos + 1 #a cada repetição, aumento 1 ano

print('em anos, demorou ', qtde_anos)
print('a populacao de A foi ', pop_a)
print('a populacao de B foi ', pop_b)

