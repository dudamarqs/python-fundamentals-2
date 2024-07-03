n1 = float(input('Insira o valor da primeira nota do aluno: '))
n2 = float(input('Insira o valor da segunda nota do aluno: '))
average = (n1 + n2)/2
if average < 5:
    print('\nAluno reprovado.')
elif average >= 5 and average < 7:
    print('\nO aluno deverá fazer a recuperação.')
else:
    print('\nAluno aprovado.')