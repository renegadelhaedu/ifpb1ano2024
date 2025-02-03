def somar_nums(inicio, fim):
    soma = 0
    for num in range(inicio, fim + 1):
        soma += num

    return soma


print(somar_nums(2, 4))