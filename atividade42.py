print('Analisando triângulos:\n')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if (a < b + c) and (b < a + c) and (c < b + a):
    if a == b and a == c:
        print('\nOs segmentos formam um triângulo equilátero.\n')
    elif (a == b) or (a == c) or (b == c):
        print('\nOs segmentos formam um triângulo isóceles.\n')
    else:
        print('\nOs segmentos formam um triângulo escaleno.\n')
else:
    print('\nOs segmentos não podem formar um triângulo.\n')