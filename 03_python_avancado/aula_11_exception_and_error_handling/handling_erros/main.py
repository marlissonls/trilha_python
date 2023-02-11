import os

def division(input):
    try:
        quociente = 1/input
    except ZeroDivisionError:
        print('ZeroDivisionError: Não é possível dividir por zero!')
    except TypeError:
        print('TypeError: Não é possível dividir um tipo int por um tipo ' + type(input).__name__ + '!')
    else:
        print(quociente)
    finally:
        print('Finalizando a execução. User: ' + os.getlogin())


division(0)                     #TypeError: Não é possível dividir por zero!
division('teste')               #TypeError: Não é possível dividir um tipo int por um tipo str!
division(['elemento','outro'])  #TypeError: Não é possível dividir um tipo int por um tipo list!
division(('elemento','outro'))  #TypeError: Não é possível dividir um tipo int por um tipo tuple!
division({'chave':'valor'})     #TypeError: Não é possível dividir um tipo int por um tipo dict!
division(10)                    #0.1
division(True)                  #1.0
division(False)                 #TypeError: Não é possível dividir por zero!
division(print('olá'))          #TypeError: Não é possível dividir um tipo int por um tipo NoneType!
division()                      #TypeError: division() missing 1 required positional argument: 'input'