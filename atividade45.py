from random import choice
from time import sleep

print('-=' * 20)
print('Jokenpô')
print('-=' * 20)

options = ['pedra', 'papel', 'tesoura']
computer = choice(options)

print('-=' * 20)
print('''Escolha:
(1) pedra
(2) papel
(3) tesoura''')

choices = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
you = int(input('Sua vez: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 20)

print(f'Você: {choices[you]}')
print(f'Computador: {computer}')
print('-=' * 20)

if (computer == 'pedra' and you == 3) or (computer == 'papel' and you == 1) or (computer == 'tesoura' and you == 2):
    print('VOCÊ PERDEU!\n')
elif (you == 1 and computer == 'tesoura') or (you == 2 and computer == 'pedra') or (you == 3 and computer == 'papel'):
    print('VOCÊ GANHOU!\n')
else:
    print('EMPATE.\n')
