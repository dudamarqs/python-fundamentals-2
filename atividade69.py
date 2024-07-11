adults = 0
men = 0
women = 0

while True: 
    print('=' * 30)
    age = int(input('Idade: '))
    sex = input('Sexo [F/M]? ').upper().strip()[0]
    print('=' * 30)
    
    if age >= 18:
        adults += 1
    if sex == 'M':
        men += 1
    if age < 20 and sex == 'F':
        women += 1
    
    question = input('Deseja continuar [S/N]? ').upper().strip()[0]
    if question == 'N':
        break

print(f'\n{adults} pessoas são maiores de 18 anos.')
print(f'Foram cadastrados {men} homens.')
print(f'Foram cadastradas {women} mulheres com menos de 20 anos.')