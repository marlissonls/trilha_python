"""
Crie uma função chamada que tenha a estrutura para receber 2 argumentos fixos e N argumentos 
nomeados e no final imprima todos os argumentos passados para essa função: 
"""

def test_args(param1, param2, *params):
    print('arg1:', param1)
    print('arg2:', param2)
    for param in params:
        print('arg' + str(params.index(param) + 3) + ':', param)

if __name__ == '__main__':
    test_args('Caruaru', 'Pernambuco', 'Nordeste', 'Brasil', 'América do Sul')