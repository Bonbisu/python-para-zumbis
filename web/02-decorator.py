def negrito(f):
    def envelope():
        return '<b>' + f() + '</b>'
    return envelope


def italico(f):
    def envelope():
        return '<i>' + f() + '</i>'
    return envelope


@negrito
@italico
def alo():
    return 'Alô mundo'


print(alo())
