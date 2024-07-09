sex = str(input('Qual é o seu sexo (F/M)? ')).upper()
while sex != 'M' and sex !='F': # or: "while sex not in 'MmFf':"
    print('Insira uma opção válida!')
    sex = str(input('\nQual é o seu sexo? ')).upper()
    