num = int(input('Qual o valor do primeiro termo? '))
razao = int(input('Qual o valor da razão? '))
enesimoTermo = num + (10 - 1) * razao
for c in range(num, enesimoTermo + razao, razao):
    print('{} '.format(c), end='→ ')
print('Fim da P.A.')