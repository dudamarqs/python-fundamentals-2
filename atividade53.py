sentence = str(input('Digite uma frase: ')).strip().upper()
words = sentence.split()
joinedWords = ''.join(words)
inverse = ''
for c in range(len(joinedWords) - 1, -1, -1):
    inverse += joinedWords[c]
if inverse == joinedWords:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
