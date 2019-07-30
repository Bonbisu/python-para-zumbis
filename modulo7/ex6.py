import urllib.request
preco = 99.99
while preco >= 4.74:
    pagina = urllib.request.urlopen(
        'http://beans.itcarlow.ie/prices-loyalty.html')
    texto = pagina.read().decode('utf8')
    inicio = texto.find('>$') + 2
    fim = texto.find('<', inicio+1)
    preco = float(texto[inicio:fim])
    print(preco)
print('Comprar! Preço: %5.2f' % preco)
