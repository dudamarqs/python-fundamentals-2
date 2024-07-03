house_price = float(input('Informe o valor da casa: R$'))
salary = float(input('Informe o seu salário: R$'))
years = int(input('Quantos anos de financiamento: '))

perc_salary = salary * 30 / 100 #calculates how much is 30% of the buyer's salary
installment = house_price / (years * 12) #calculates the value of the installment
print('\nPara uma casa de R${:.2f}, o valor das prestações será de R${:.2f} durante {}anos.'.format(house_price, installment, years))

if installment <= perc_salary: #compares the value of the instalments and the buyer's salary
    print('O empréstimo foi concedido.\n')
else:
    print('\nO empréstimo foi negado.\n')