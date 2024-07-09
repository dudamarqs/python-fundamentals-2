num = int(input('Qual o valor do primeiro termo? '))
razao = int(input('Qual o valor da razão? '))

termo = num
cont = 1

print('\nOs 10 primeiros termos da P.A.:')
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim.')
