total = count = 0
more_than1000 = cheaper = 0

while True: 
    print('=' * 30)
    prod = str(input('Produto: '))
    price = float(input('Preço: R$'))
    print('=' * 30)
    count += 1
    total += price

    if price > 1000:
        more_than1000 += 1
    if count == 1:
        cheaper = price
    else:
        if price < cheaper:
            cheaper = price

    question = ' '
    while question not in 'SsNn':
        question = input('Deseja continuar (S/N)? ').upper().strip()[0]
    if question == "N":
        break

print('{:-^40}'.format('\nFim do programa.'))
print(f'O valor total da compra foi R${total}.')
print(f'{more_than1000} produto(s) custa(m) mais de R$1000,00')
print(f'O produto mais barato custa R${cheaper}.')