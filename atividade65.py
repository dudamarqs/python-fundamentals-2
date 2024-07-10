answer = 'S'
sum = quant = average = 0
while answer in 'Ss': 
    num = int(input('Digite um número: '))
    sum += num
    quant += 1
    answer = input('Deseja continuar (S/N)? ').upper().strip()[0]
    if quant == 1:
        highest = smallest = num
    else:
        if num > highest:
            highest = num
        if num < smallest:
            smallest = num
average = sum / quant
print('\nA média dos {} números digitados é {}.'.format(quant, average))
print('O maior número digitado foi {} e o menor foi {}.'.format(highest, smallest))