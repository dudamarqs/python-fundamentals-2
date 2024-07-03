n1 = float(input('Insira o valor da primeira nota do aluno: '))
n2 = float(input('Insira o valor da segunda nota do aluno: '))
average = (n1 + n2)/2
print('\nA média do aluno é {:.1f}.'.format(average))
if average < 5:
    print('Situação do aluno: reprovado.')
elif average >= 5 and average < 7:
    print('Situação do aluno: recuperação.')
else:
    print('Situação do aluno: aprovado.')