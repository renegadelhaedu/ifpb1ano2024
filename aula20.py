#estrutura de repetição
#for para tabuada

num_tabuada = int(input('digite o número para saber a tabuada dele'))

for num in range(11):
    resultado = num_tabuada * num
    #print(num_tabuada, ' X ', num, ' = ', resultado)
    print(f'{num_tabuada}  X  {num} = {resultado}')