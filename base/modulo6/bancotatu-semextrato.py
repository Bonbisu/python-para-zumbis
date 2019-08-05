from tatu import Cliente
from tatu import Conta


def retrieve_name(x, Vars=vars()):
    for k in Vars:
        if type(x) == type(Vars[k]):
            if x is Vars[k]:
                return k
    return None


def tranferir(origem, destino, valor):
    origem.saque(valor)
    destino.deposito(valor)
    cliente1 = origem.clientes[0]
    cliente2 = destino.clientes[0]
    print('Tranferido R$ %d de [%s - %s] para [%s - %s]' %
          (valor, cliente1.nome, origem.numero, cliente2.nome, destino.numero))


maria = Cliente('Maria da Silva', '777-9474')
jose = Cliente('José da Silva', '888-9887')
base = 'Nome: %s Telefone %s'
print(base % (maria.nome, maria.telefone))
print(base % (jose.nome, jose.telefone))

conta1 = Conta([jose], 1, 1000)
conta2 = Conta([maria, jose], 2, 500)

conta1.resumo()
conta2.resumo()
# print(conta1.__dict__)


tranferir(conta1, conta2, 100)
conta1.resumo()
conta2.resumo()
