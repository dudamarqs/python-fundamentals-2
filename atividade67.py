while True:
    num = int(input('Digite um número para ver sua tabuada (número negativo para finalizar): '))
    
    if num < 0:
        break

    print('=' * 50)
    print(f'Tabuada do {num}:')
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('=' * 50)
    
print('\nPrograma encerrado.\n')