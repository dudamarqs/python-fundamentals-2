count = sum = 0

while True:
    n = int(input('Digite um número (digite 999 para finalizar): '))
    if n == 999:
        break
    sum += n
    count += 1
print('\nA soma do(s) {} valor(es) digitado(s) é {}.\n'.format(count, sum))