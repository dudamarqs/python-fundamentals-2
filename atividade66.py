count = 0
sum = 0

while True:
    num = int(input('Digite um número (999 para finalizar): '))
    if num == 999:
        break
    sum += num
    count += 1
print(f'A soma dos {count} números digitados é {sum}.')