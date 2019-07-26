from tatu2 import Cliente
from tatu2 import Conta

maria = Cliente('Maria da Silva', '777-9474')
jose = Cliente('José da Silva', '888-9887')
conta1 = Conta([jose], 1, 1000)
conta2 = Conta([maria, jose], 2, 500)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()
