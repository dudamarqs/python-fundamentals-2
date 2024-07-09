from random import randint

comp = randint(0,10)
attempts = 0
correct = False

print('-=' * 34)
print('Pensei em um número entre 0 e 10. Veja se consegue descobrir qual é!')
print('-=' * 34)

player = int(input('Em que número eu pensei? '))
while not correct:
    player = int(input('\nEm que número eu pensei? '))
    attempts = attempts + 1
    if player == comp:
        correct = True
    else:
        if player < comp:
            print('Mais... tente de novo.')
        elif player > comp:
            print('Menos... tente de novo.')

print('\nParabéns! Você acertou!')
print('Você precisou de {} tentativas.'.format(attempts + 1))
