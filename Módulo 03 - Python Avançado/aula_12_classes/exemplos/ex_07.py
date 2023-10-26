class Funcionario:
    #inicialização dos atributos
    def __init__(self, nome, cpf, salario=0):
        pass
    #propriedades e outros métodos
    def get_bonificacao(self):
	    return self._salario * 1.2

class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self.__total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if(hasattr(obj,	'get_bonificacao')):
            self.__total_bonificacoes += obj.get_bonificacao()
        else:
            print('instância de {} não implementa o método get_bonificacao()'.format(self.__class__.__name__))	