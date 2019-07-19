'''
Imprima as tabuadas de 1 a 10
'''

tabuada = 1

while tabuada <= 10:
    multiplicador = 1
    print('\nTabuada do %d' % tabuada)
    while multiplicador <= 10:
        print('%d x %d = %d' % (tabuada, multiplicador, tabuada*multiplicador))
        multiplicador += 1
    tabuada += 1
