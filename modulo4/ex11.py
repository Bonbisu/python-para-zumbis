with open('ola.html', 'w', encoding='utf-8')as file:
    file.write('''<!doctype html>
    <html lang="pt-BR">
    <head>
    <meta charset="utf-8">
    <title>Título da página</title>
    </head>
    <body>
    Olá!
    </body>
    </html>''')
file.close()
