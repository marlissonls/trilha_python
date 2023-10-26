class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes
    
    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()
        
    @property
    def total_bonificacoes(self):
	    return self._total_bonificacoes

class Funcionario:
    pass

class Gerente(Funcionario):
    pass

if __name__ == '__main__':
    funcionario = Funcionario('João', '111111111-11', 2000.0)
    print("bonificacao funcionario: {}".format(funcionario.get_bonificacao()))
    gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0)
    print("bonificacao gerente: {}".format(gerente.get_bonificacao()))
    controle = ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)
    print("total: {}".format(controle.total_bonificacoes))

""" 
que	gera a saída:
bonificacao funcionario: 200.0
bonificacao gerente: 1500.0
total: 1700.0
"""