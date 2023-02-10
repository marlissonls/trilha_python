def func_args(*args):
    print(f'tipo: {type(args)} conteúdo: {args}')
    for arg in args:
        print(f'tipo: {type(arg)} conteúdo: {arg}')


func_args(1, 'A', {'valor': 10})