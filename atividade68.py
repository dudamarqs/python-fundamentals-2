from random import randint

v = 0
while True:
    player = int(input('Jogue um valor: '))
    comp = randint(0, 11)
    total = player + comp
    answer = ' '
    while answer not in 'PpIi':
        answer = str(input('Par ou ímpar [P/I]? ')).upper().strip()[0]
    print(f'Você jogou {player} e o computador jogou {comp}. O total foi {total}.')
    if answer == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    if answer == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('\nVamos jogar novamente!')
print(f'Você ganhou {v} vezes!')
        

