import urllib.request
pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
texto = pagina.read().decode('utf-8')
inicio = texto.find('>$') + 2
fim = texto.find('<', inicio+1)
preco = float(texto[inicio:fim])

if preco < 4.74:
    print('Comprar! Preço: %5.2f' % preco)
