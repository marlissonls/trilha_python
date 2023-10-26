from customized_errors import ZeroOrNegativeValueError
from typing import List

def validateSides(numSides: int, polygonType: str) -> List[float]:
    """ This function takes a number of sides and the polygon type name and returns a list of validated side sizes """

    sides = []
    for sideIterator in range(numSides):
        print(f'\n{sideIterator + 1}º lado do {polygonType}.')
        while True:
            try:
                side = float(input('\nInforme um número decimal ou inteiro: ').replace(',', '.'))
                if side <= 0:
                    raise ZeroOrNegativeValueError
            except ValueError:
                print('\nValueError: Os valores informados não podem ser convertidos para números decimais!')
            except ZeroOrNegativeValueError:
                print('\nZeroOrNegativeValueError: O valor do tamanho do lado não pode ser igual a zero ou negativo!')
            else:
                sides.append(side)
                break
    return sides