""" 
Crie a classe Polygon com um construtor que recebe “sides: List[float]” e um método “display_sides() -> List[float]”.
Crie também a classe Triangle que herda o Polygon e implementa o “find_area() -> float”.
"""
from abc import ABC
from typing import List
import math

class TriangleError(Exception):
    "Raised when the quantity of numbers inserted on input are different of 3."

class ZeroOrNegativeValueError(Exception):
    "Raised when a determined value is zero or negative."

class Polygon(ABC):
    """ Esta classe foi definida como uma classe abstrata porque ela não remete a nenhum polígono específico """

    def __init__(self, sides: List[float]) -> None:
        self._sides = sides
       
    def display_sides(self) -> List[float]:
        """ Retorna uma List[float] com os lados do polígono """
        return self._sides

class Triangle(Polygon):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
    
    def find_area(self) -> float:
        """ 
        Este método usa o atributo _sides que contém uma Lista[lado: float, lado: float, lado: float] para calcular a área de um triângulo.
        O Calculo da área é feito usando a Fórmula de Herão de Alexandria: A = [p(p-a)(p-b)(p-c)]^(0.5).
        Onde A = área do triângulo, p = perímetro/2 e a, b e c = lados do triângulo.
        """
        [ a, b, c ] = self._sides
        p = sum([ a, b, c ]) / 2
        Area = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return Area

def validateSides(numSides: int, polygonType: str) -> List[float]:
    """
    Esta função recebe um número de lados e o nome de tipo de polígono e
    retorna uma lista com os tamanhos dos lados validados
    """
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

def validateTriangle(numTriangleSides: int) -> List[float]:
    """Esta função obtém os lados do triângulo e retorna uma lista dos lados validados do triângulo"""

    while True:
        try:
            sides = validateSides(numTriangleSides, 'triângulo')
            
            boolean_1 = sides[0] + sides[1] <= sides[2]
            boolean_2 = sides[0] + sides[2] <= sides[1]
            boolean_3 = sides[1] + sides[2] <= sides[0]

            if boolean_1 or boolean_2 or boolean_3:
                raise TriangleError
        except TriangleError:
            print('\nTriangleError: Os lados informados não podem formar um triâgulo!')
            print('Motivo: O tamanho de um dos lados é igual ou superior à soma dos tamanhos dos outros dois lados.')
        else:
            return sides

def main() -> None:
    """
    Esta função pede os lados de um triângulo, cria uma instância de um Triangle, 
    mostra uma lista com os lados do triângulo e mostra o valor da área do triângulo
    """
    
    triangleSides = validateTriangle(3)
    triangulo = Triangle(triangleSides)

    print(f'\nLados do triângulo: {triangulo.display_sides()}')
    print(f'\nÁrea do triângulo: {round(triangulo.find_area(), 3)}')

if __name__ == '__main__':
    main()