weight = float(input('Informe seu peso (em kg): '))
height = float(input('Informe sua altura (em m): '))
bmi = weight / (height ** 2) # BMI (IMC em português): Body Mass Index

if bmi < 18.5:
    print('\nVocê está abaixo do peso ideal.')
elif 18.5 <= bmi < 26:
    print('\nVocê está no peso ideal.')
elif 24 < bmi < 31:
    print('\nVocê está com sobrepeso.')
elif 29 < bmi < 41:
    print('\nVocê está com obesidade.')
else:
    print('\nVocê está com obesidade mórbida.')