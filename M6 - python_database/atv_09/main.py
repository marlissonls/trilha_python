from modules.db import conn
from modules.create_tables import create_tables
from modules.populate_tables import populate_tables
from modules.create_views import create_views
from modules.delete_from_table import delete_from_table
from modules.analyse_views_performance import analyse_views_performance
from modules.insert_performance_results import insert_performance_results
from modules.show_performance_results import show_performance_results

while True:
    print('\n')
    print('1 - Criar tabelas.')
    print('2 - Popular as tabelas com os dados.')
    print('3 - Criar views.')
    print('4 - Limpar dados das tabelas usuario e contato.')
    print('5 - Realizar busca dos dados de um usuário.')
    print('6 - Inserir resultado da busca na tabela compare_results.')
    print('7 - Monstrar tabela compare_results.')
    print('8 - Encerrar operações')

    option = input('\nSelecione o número de uma das operações: ')
    print('\n')
    match option:
        case '1':
            create_tables()

        case '2':
            population = int(input('Digite o número da quantidade de dados: '))
            populate_tables(population)

        case '3':
            create_views()

        case '4':
            delete_from_table()

        case '5':
            print('Escolha uma opção de busca query usando INNER JOIN e GROUP para devolver o usuário com os respectivos telefones.')
            print('1 - Fazer a busca usando o comando SQL predefinido.')
            print('2 - Fazer a busca usando a view predefinida.')
            print('3 - Fazer a busca usando a view materializada predefinida.')
            option = input('Digite a opção: ')
            if option in ('1', '2', '3'):
                result = analyse_views_performance(option)
                print(result)
            else: print('Opção inválida.')

        case '6':
            req = input('Informe a requisição: ')
            mil = input(f'Informe o tempo da requsicao "{req}" com população de 1 mil registros: ')
            dezmil = input(f'Informe o tempo da requsicao "{req}" com população de 10 mil registros: ')
            cemmil = input(f'Informe o tempo da requsicao "{req}" com população de 100 mil registros: ')
            milhao = input(f'Informe o tempo da requsicao "{req}" com população de 1 milhão registros: ')
            insert_performance_results(req, mil, dezmil, cemmil, milhao)

        case '7':
            result = show_performance_results()
            print(result)
            
        case '8':
            print('Operações encerradas!')
            conn.close()
            break
        
        case _:
            print('Opção inválida!')