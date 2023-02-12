import datetime
class Historico:
    def	__init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    def	imprime(self):
        print("data	abertura: {}".format(self.data_abertura))
        print("transações: ")
        for	t in self.transacoes:
            print("-", t)

class Cliente:
    def	__init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    _total_contas = 0
    __slots__ = ['_numero', '_titular', '_saldo', '_limite']

    def	__init__(self, numero, cliente,	saldo, limite = 1000.0):
        self._numero	= numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1

    def	deposita(self, valor):
        self._saldo += valor
        self._historico.transacoes.append("depósito de {}".format(valor))

    def	saca(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            self._historico.transacoes.append("saque de {}".format(valor))
            return True
    
    def	extrato(self):
        print("numero: {}\nsaldo: {}".format(self._numero, self._saldo))
        self._historico.transacoes.append("tirou	extrato - saldo de {}".format(self._saldo))

    def	transfere(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self._historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True

    def	pega_saldo(self):
        return self._saldo
    
    @staticmethod
    def get_total_contas():
        return Conta._total_contas


class Conta:
    _total_contas = 0

    def	__init__(self):
        type(self)._total_contas += 1

    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

""" conta = Conta('123-4', 'João', 120.0, 1000.0)
conta.deposita(20.0)
conta.extrato()
#numero: '123-4'
#saldo:	140.0
conta.saca(15)
conta.extrato()
#numero:	'123-4'
#saldo:	125.0 """

""" cliente1	=	Cliente('João',	'Oliveira',	'11111111111-11')
cliente2	=	Cliente('José',	'Azevedo',	'222222222-22')
conta1	=	Conta('123-4',	cliente1,	1000.0)
conta2	=	Conta('123-5',	cliente2,	1000.0)
conta1.deposita(100.0)
conta1.saca(50.0)
conta1.transfere_para(conta2,	200.0)
conta1.extrato
#numero:	123-4	
#saldo:	850.0
conta1.historico.imprime()
#data	abertura:	2018-05-10	19:44:07.406533
#transações:	
#-	depósito	de	100.0
#-	saque	de	50.0
#-	saque	de	200.0
#-	transferencia	de	200.0	para	conta	123-5
#-	tirou	extrato	-	saldo	de	850.0
conta2.historico.imprime()
#data	abertura:	2018-05-10	19:44:07.406553
#transações:	
#-	depósito	de	200.0 """

