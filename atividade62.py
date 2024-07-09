num = int(input('Qual o valor do primeiro termo? '))
razao = int(input('Qual o valor da razão? '))

termo = num
cont = 1
total = 0
mais = 10

print('\nOs 10 primeiros termos da P.A.:')

while mais != 0:
    total = total + 10
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1

    print('pausa.')
    mais = int(input('\nQuantos valores quer mostrar a mais? (Digite 0 para finalizar)'))
print('\nProgressão finalizada com {} termos.'.format(total))