from datetime import date

current_year = date.today().year
cont = 0
adults = 0
minors = 0
for cont in range(1, 8):
    year = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(cont)))
    age = current_year - year
    if age >+ 21:
        adults += 1
    else:
        minors += 1
print('Ao todo tem {} pessoas maiores de idade e {} menos de idade.'.format(adults, adults))
