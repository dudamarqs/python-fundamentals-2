from datetime import date

year_birth = int(input('Em que ano você nasceu? '))
year = date.today().year
age = year - year_birth
print('O atleta tem {} anos.'.format(age))

if age < 10:
    print('Categoria: MIRIM.')
elif 9 < age < 15:
    print('Categoria: INFANTIL.')
elif 14 < age < 20:
    print('Categoria: JÚNIOR.')
elif 19 < age < 25:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')