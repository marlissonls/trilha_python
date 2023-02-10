def func_missao_dificil(nome, *args, funcao='agente', **kwargs):
    print(f'Nome do agente: {nome}')
    print(f'Função: {funcao}')
    print(args)
    print(kwargs)

params = {
            'id_agente': '007',
            'proxima_missao': 'Impossível'
         }

func_missao_dificil(
    'James Bond',
    'Missao 1',
    'Missão 2',
    **params
)