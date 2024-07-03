name = input('Informe seu nome completo: ')
year_birth = int(input('Em que ano você nasceu? '))
current_year = int(input('Informe o ano atual: '))
age = current_year - year_birth

if age < 18:
    years = 18 - age
    days = int(years*365.25)
    print('\nO jovem {} terá que se apresentar no quartel em {} dias ({} anos).'.format(name, days, years))
elif age == 18:
    print('\nO jovem {} deve se apresentar no quartel este ano.'.format(name))
elif age > 18:
    years = age - 18
    days = int(years*365.25)
    print('\nJá passou {} dias ({} anos) do prazo de alistamento de {}.'.format(days, years, name))