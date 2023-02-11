import os

Any = int | float | str | bool | bytes | list | tuple | dict | set | object | frozenset

def division(input: Any) -> None:
    """
    This function takes an input that can be any value or type and tries to calculate 1/input. 
    It raises some exception/error or the result of division. And at the end | it shows a message with the user name.
    """
    try:
        quociente = 1/input
    except ZeroDivisionError:
        print('ZeroDivisionError: Não é possível dividir por zero!')
    except TypeError:
        print('TypeError: Não é possível dividir um tipo int por um tipo {0}!'.format(type(input).__name__))
    else:
        print(quociente)
    finally:
        print('Finalizando a execução. User: {0}.\n'.format(os.getlogin().upper()))

def main() -> None:
    """
    This function is the main function which just call division function with some input values
    """
    print("This program tries to calculate 1/input, where the variable input assume the values of this list:\n")
    
    inputs = (0, 'teste', ['elemento','outro'], ('elemento','outro'), {'chave':'valor'}, print('funcão print() passada como argumento'), 10, True, False, None)

    print(inputs)
    print('\n\n')

    for input in inputs:
        division(input)
    
    division(variavelIndefinida)  # Chamada com uma variavel indefinida.
    variavelDeletada = 1
    del variavelDeletada
    division(variavelDeletada)    # Chamada com uma variavel deletada.
    division()                    # Chamada sem fornecer um argumento.
    

if __name__ == '__main__':
    main()


"""
---Resultados---

division(0)                                                TypeError: Não é possível dividir por zero!
division('teste')                                          TypeError: Não é possível dividir um tipo int por um tipo str!
division(['elemento','outro'])                             TypeError: Não é possível dividir um tipo int por um tipo list!
division(('elemento','outro'))                             TypeError: Não é possível dividir um tipo int por um tipo tuple!
division({'chave':'valor'})                                TypeError: Não é possível dividir um tipo int por um tipo dict!
division(print('funcão print() passada como argumento'))   TypeError: Não é possível dividir um tipo int por um tipo NoneType!
division(10)                                               0.1
division(True)                                             1.0
division(False)                                            TypeError: Não é possível dividir por zero!
division(None)                                             TypeError: Não é possível dividir um tipo int por um tipo NoneType!
division(variavelIndefinida)                               NameError: name 'variavelIndefinida' is not defined
division(variavelDeletada)                                 UnboundLocalError: local variable 'variavelDeletada' referenced before assignment
division()                                                 TypeError: division() missing 1 required positional argument: 'input'
"""

"""
Log de erros do mypy

main.py:11: error: Unsupported operand types for / ("int" and "str")  [operator]
main.py:11: error: Unsupported operand types for / ("int" and "bytes")  [operator]
main.py:11: error: Unsupported operand types for / ("int" and "List[Any]")  [operator]
main.py:11: error: Unsupported operand types for / ("int" and "Tuple[Any, ...]")  [operator]
main.py:11: error: Unsupported operand types for / ("int" and "Dict[Any, Any]")  [operator]
main.py:11: error: Unsupported operand types for / ("int" and "Set[Any]")  [operator]
main.py:11: error: Unsupported operand types for / ("int" and "object")  [operator]
main.py:11: error: Unsupported operand types for / ("int" and "FrozenSet[Any]")  [operator]
main.py:11: note: Right operand is of type "Union[int, float, str, bool, bytes, List[Any], Tuple[Any, ...], Dict[Any, Any], Set[Any], object, FrozenSet[Any]]"
main.py:35: error: Name "variavelIndefinida" is not defined  [name-defined]
main.py:38: error: Trying to read deleted variable "variavelDeletada"  [misc]
main.py:39: error: Missing positional argument "input" in call to "division"  [call-arg]
Found 11 errors in 1 file (checked 1 source file)
"""