print('-=' * 10)
print('TABUADA')
print('-=' * 10)
num = int(input('Digite um número: '))
print('-=' * 10)
print('Tabuada do {}:'.format(num))
for c in range(1, 10+1):
    print('{} x {} = {}'.format(num, c, num*c))
print('-=' * 10)