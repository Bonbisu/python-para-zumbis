from tkinter import *


def salvar_dados():
    f = open('encomenda.txt', 'a')
    f.write('Destino: ')
    f.write('%s\n' % destino.get())
    f.write('Descrição: ')
    f.write('%s\n' % descricao.get())
    f.write('Endereço: ')
    f.write('%s\n' % endereco.get('1.0', END))
    descricao.delete(0, END)
    endereco.delete('1.0', END)
    f.close()


app = Tk()
app.title('HeadEx Logística e Transporte')
Label(app, text='Destino: ').pack()
destino = StringVar()
destinos = ['São Paulo', 'Bahia', 'Rio de Janeiro']
[Radiobutton(app, variable=destino, text=d, value=d).pack() for d in destinos]
Label(app, text='Descrição: ').pack()
descricao = Entry(app)
descricao.pack()
Label(app, text='Endereço: ').pack()
endereco = Text(app)
endereco.pack()

Button(app, text='Salvar encomenda', command=salvar_dados).pack()
app.mainloop()
