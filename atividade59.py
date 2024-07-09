from time import sleep

number1 = int(input('Digite um valor: '))
number2 = int(input('Digite outro valor: '))

option = 0

while option != '5':
    print('''\nMenu de opções:
        (1) Somar
        (2) Multiplicar
        (3) Maior
        (4) Novos números
        (5) Sair do programa''')
    option = input('\nEscolha uma opção: ')

    if option == '1':
        print('Soma dos dois valores: {} + {} = {}.'.format(number1, number2, number1 + number2))
    elif option == '2':
        print('Multiplicação dos dois números: {} x {} = {}.'.format(number1, number2, number1 * number2))
    elif option == '3':
        greater = number1 if number1 > number2 else number2
        print('Maior valor entre os dois: {}.'.format(greater))
    elif option == '4':
        number1 = int(input('\nDigite um novo valor: '))
        number2 = int(input('Digite outro novo valor: '))
    elif option == '5':
        print('Saindo do programa...')
        sleep(1)
    else:
        print('Opção inválida!. Tente novamente.')
print('\nPrograma encerrado.')