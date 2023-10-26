import abc
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

class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes
    
    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()
# OUTRA FORMA DE ESCREVER O MÉTODO
    def	registra(self, obj):
        if(hasattr(obj,	'get_bonificacao')):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('instância de {} não implementa o método get_bonificacao()'.format(self.__class__.__name__))
# OUTRA FORMA DE ESCREVER O MÉTODO
    def	registra(self, obj):
        if(isinstance(obj,	Funcionario)):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('instância de {} não implementa o método get_bonificacao()'.format(self.__class__.__name__))	
# OUTRA FORMA DE ESCREVER O MÉTODO
    def registra(self, funcionario):
        try:
            self._total_bonificacoes += funcionario.get_bonificacao()
        except AttributeError as error:
            print(error)
        
    @property
    def total_bonificacoes(self):
	    return self._total_bonificacoes

class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    @abc.abstractmethod
    def get_bonificacao(self):
        return self._salario * 0.10

class FuncionarioAutenticavel(Funcionario, abc.ABC):
    @abc.abstractmethod  # Deve ser levado em consideração
    def	autentica(self,	senha):
        pass # verifica se a senha confere

class AutenticavelMixIn:
    def autentica(self,	senha):
        pass # verifica se a senha confere

class Autenticavel(abc.ABC):
    """
    Classe abstrata que contém operações de um objeto autenticável.
    As subclasses concretas devem sobrescrever o método autentica.
    """
    @abc.abstractmethod
    def autentica(self,	senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False

class HoraExtraMixIn:
    def	calcula_hora_extra(self, horas):
        pass # calcula horas extras



class Gerente(Funcionario, Autenticavel, HoraExtraMixIn):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False

    def get_bonificacao(self):
        return self._salario * 0.15
    
    def get_bonificacao(self):  ### Este é outro exemplo de get_bonificação caso se queira herdar as informações
        return super().get_bonificacao() + 1000

Autenticavel.register(Gerente) ## Agora lascou. É uma atribuição em tempo de execução

class Diretor(Funcionario, AutenticavelMixIn):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)
    
    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False

    def get_bonificacao(self):
        return self._salario * 0.30

class SistemaInterno:
    def	login(self,	obj):
        if (hasattr(obj, 'autentica')):
            obj.autentica()
            return True
        else:
            print('{} não é autenticável'.format(self.__class__.__name__))
            return False

class SistemaInterno:
    def login(self, obj):
        if (isinstance(obj, Autenticavel)):
            obj.autentica(obj.senha)
            return True
        else:
            print("{} não é autenticável".format(self.__class__.__name__))
            return False

class Cliente(AutenticavelMixIn):
    def __init__(self, nome, sobrenome, cpf, senha):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._senha = senha

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False
    
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

class C: 
    @classmethod 
    def fun(cls, arg1, arg2):
        pass

class AtendimentoMixIn:
    def cadastra_atendimento(self):
        pass # faz cadastro atendimento
    def atende_cliente(self):
        pass # faz atendimento

class Escriturario(Funcionario, AtendimentoMixIn):
    pass

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