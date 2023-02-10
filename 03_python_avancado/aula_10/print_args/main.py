"""
Crie uma função chamada que tenha a estrutura para receber 2 argumentos fixos e N 
argumentos nomeados e no final imprima todos os argumentos passados para essa função:
"""

Trio = str | int | float

def print_args(param1: Trio, param2: Trio, **kwparams: Trio ) -> None:
    """
    This function takes two fixed arguments and an unknown number of named arguments. It then prints out all received args.
    """
    print('arg1 = ' + str(param1))
    print('arg2 = ' + str(param2))
    for key, value in kwparams.items():
        print(str(key) + ' = ' + str(value))

if __name__ == '__main__':
    print_args('carne', 'varejo', agua = 'aquática', terra = 'terrestre', chuva = 'molhada', calor = 'quente')
