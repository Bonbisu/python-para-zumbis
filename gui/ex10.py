from tkinter import *
from tkinter import messagebox


def salvar_dados():
    try:
        f = open('encomenda.txt', 'a')
        f.write('Destino: ')
        f.write('%s\n' % destino.get())
        f.write('Descrição: ')
        f.write('%s\n' % descricao.get())
        f.write('Endereço: ')
        f.write('%s\n' % endereco.get('1.0', END))
        destino.set(None)
        descricao.delete(0, END)
        endereco.delete('1.0', END)
    except Exception as excecao:
        messagebox.showerror(
            'Erro!', 'Não foi possivel gravar a encomenda\n%s' % excecao)
    f.close()


def ler_destinos(file):
    destinos = []
    f = open(file)
    for l in f:
        destinos.append(l.rstrip())
    f.close()
    destinos.sort()
    return destinos


app = Tk()
app.title('HeadEx Logística e Transporte')
Label(app, text='Destino: ').pack()
destino = StringVar()
destino.set(None)
destinos = ler_destinos('destinos.txt')
OptionMenu(app, destino, *destinos).pack()
Label(app, text='Descrição: ').pack()
descricao = Entry(app)
descricao.pack()
Label(app, text='Endereço: ').pack()
endereco = Text(app)
endereco.pack()

Button(app, text='Salvar encomenda', command=salvar_dados).pack()
app.mainloop()
