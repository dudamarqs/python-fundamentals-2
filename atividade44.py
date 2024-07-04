price = float(input('Preço total das compras: R$'))
print('''Formas de pagamento:
(1) à vista dinheiro/cheque
(2) à vista no cartão
(3) 2x no cartão
(4) 3x ou mais no cartão\n''')
option = int(input('Qual a forma de pagamento? '))

if option == 1:
    total = price - (price * 10/100)
elif option == 2:
    total = price - (price * 5/100)
elif option == 3:
    total = price
    installment = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(installment))
elif option == 4:
    total = price + (price * 20/100)
    num_inst = int(input('\nInforme quantas parcelas: '))
    installment = total / num_inst
    print('Sua compra será parcelada em {}x de R${:.2f} com 20% de juros.'.format(num_inst, installment))
else:
    print('Opção inválida.')
    total = price
print('\nValor final da compra: R${:.2f}.'.format(total))
