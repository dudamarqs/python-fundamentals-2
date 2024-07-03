year_birth = int(input('Em que ano você nasceu? '))
age = 2024 - year_birth

if age < 10:
    print('Categoria: MIRIM.')
elif age > 9 and age < 15:
    print('Categoria: INFANTIL.')
elif age > 14 and age < 20:
    print('Categoria: JÚNIOR.')
elif age == 20:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')