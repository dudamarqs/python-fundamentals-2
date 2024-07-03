number = int(input('Digite um número: '))
option = input('\nEscolha uma opção:\n(1) binário\n(2) octal\n(3) hexadecimal\n Opção: ')

if option == '1':
    print('\nO valor binário de {} é {}.'.format(number, bin(number)[2:]))
elif option == '2':
    print('\nO valor octal de {} é {}.'.format(number, oct(number)[2:]))
elif option == '3':
    print('\nO valor hexadecimal de {} é {}.'.format(number, hex(number)[2:]))
else:
    print('\nOpção inválida!')