num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[033m', end=' ')
        tot += 1
    else:
        print('\033[034m', end=' ')
    print('{} '.format(c), end=' ')
print('\nO número {} foi dívisível {} vezes.'.format(num, tot))
if tot == 2:
    print('{} é um número primo.\n'.format(num))
else:
    print('{} não é um número primo.\n'.format(num))