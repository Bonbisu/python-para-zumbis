'''
Validador de enderaços de IP
'''


def ip_ok(ip):
    """
    Return True if valid IP
    """
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True


with open('IPS.txt') as file:
    for linha in file.readlines():
        if ip_ok(linha):
            with open('validos.txt', 'a') as validos:
                validos.write(linha)
        else:
            with open('invalidos.txt', 'a') as invalidos:
                invalidos.write(linha)
