cont = 0
sum = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        sum = sum + c
print('A soma dos {} valores solicitados é {}.'.format(cont, sum))
