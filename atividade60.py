from math import factorial

num = int(input('Digite um valor para calcular o seu fatorial: '))
c = num 
fact = 1

print('\nCalculando {}!:'.format(num))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fact *= c
    c -= 1
print('{}'.format(fact))