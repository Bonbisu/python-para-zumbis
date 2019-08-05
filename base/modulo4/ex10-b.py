'''
Validador de enderaços de IP
'''


def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        print(byte)
        if int(byte.rstrip()) > 255:
            return False
    return True


file = open('IPS.txt')
validos = open('validos.txt', 'w')
invalidos = open('invalidos.txt', 'w')

for linha in file.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)
file.close()
validos.close()
invalidos.close()
