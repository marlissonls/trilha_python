def func_kwargs(**kwargs):
    print(f'tipo: {type(kwargs)} contuedo: {kwargs}')
    for key, value in kwargs.items():
        print(f'atributo: {key}, valor: {value}')

func_kwargs(nome='James', sobrenome='Bond', cargo='Agente 007')