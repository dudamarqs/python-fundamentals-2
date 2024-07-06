age_sum = 0
age_average = 0
older_man = 0
older_man_name = ''
tot_woman20 = 0

for p in range(1, 5):
    print('\n{}ª pessoa:'.format(p))
    name = str(input(('Nome: ')))
    age = int(input('Idade: '))
    sex = str(input('Sexo (F/M): ')).strip()
    age_sum += age
    if p == 1 and sex in 'Mm':
        older_man = age
        older_man_name: name
    if sex in 'Mm' and age > older_man:
        older_man = age
        older_man_name = name
    if sex in 'Ff' and age > 20:
        tot_woman20 += 1
age_average = age_sum / 4
print('A média de idade do grupo é de {} anos.'.format(age_average))
print('O homem mais velho tem {} anos e se chama {}.'.format(older_man, older_man_name))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(tot_woman20))