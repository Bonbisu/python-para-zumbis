''''
Criptografia de Cesar feito por uma menida de 12 anos
ord(s) => retorna o unicode da letra
chr(i) => retorna a letra pelo unicode
'''


def esconde(msg):
    s = ''
    for c in msg:
        s += chr(ord(c)+30000)
    return s


def mostra(msg):
    s = ''
    for c in msg:
        s += chr(ord(c)-30000)
        return s


s = input('Digite uma frase: ')
print('Mensagem criptografada:', esconde(s))
