sum = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        sum += n
        cont += 1
print('\nA soma dos {} números pares é {}'.format(cont, sum))