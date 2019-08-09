'''
Questão A (Vestibular FATEC 2008). Uma escola do Ensino Fundamental ofereceu a alguns de seus alunos
um passeio ao zoológico. Para tanto, a escola pretende gastar EXATAMENTE 93 reais e sabe que o ingresso
do zoológico custa 5 reais para os menores de 12 anos e 7 reais os que têm 12 anos ou mais. Elabore um
algoritmo que retorne o número máximo de alunos que a escola pode levar ao zoológico considerando
todos os valores como inteiros. O seu programa deve ter uma abordagem genérica e não levar em conta
peculiaridades nos dados fornecidos.
Questão B. Conversor de decimal para romano. Você deverá programar um algoritmo em Python que
traduza um número lido no sistema arábico para romano. Evite fazer muitos “ifs”. A idéia é usar um
comando while para analisar cada casa decimal e gerar os caracteres romanos diferentemente para cada
iteração. Exemplo 2011 = MMXI em romano. Não precisa testar até o infinito, basta de 1 até 2013.
Questão C. Faça um programa que calcule o valor aproximado de pi com n termos, segundo a fórmula
abaixo. No exemplo são visíveis 4 termos.

pi = 4/1 - 4/3 + 4/5 - 4/7
'''


def questaoA():
    budget = 93
    max_peq = budget//5
    while (budget - max_peq*5) % 7 != 0:
        max_peq -= 1
    max_gran = (budget - max_peq*5)//7
    return '%d pequenos e %d grandes' % (max_peq, max_gran)


print(questaoA())


def to_roman(n):
    uni = [''] + 'I II III IV V VI VII VIII IX'.split()
    dez = [''] + 'X XX XXX XL L LX LXX LXXX XC'.split()
    cen = [''] + 'C CC CCC CD D DC DCC DCCC CM'.split()
    mil = [''] + 'M MM MMM ~IV ~V ~VI ~VII ~VIII ~IX'.split()
    m, n = n // 1000, n % 1000
    c, n = n//100, n % 100
    d, n = n//10, n % 10
    u = n
    return mil[m] + cen[c] + dez[d] + uni[u]


print(to_roman(1991))


def to_pi(n):
    k = 1
    impar = 1
    pi = 0
    while k <= n:
        if k % 2 == 1:
            pi += 4/impar
        else:
            pi -= 4/impar
        k += 1
        impar += 2
    return pi


print(to_pi(1000))
