""" 
Crie a classe Polygon com um construtor que recebe “sides: List[float]” e um método “display_sides() -> List[float]”.
Crie também a classe Triangle que herda o Polygon e implementa o “find_area() -> float”.
"""

from abc import ABC
from typing import List
import math

class TriangleError(Exception):
    "Raised when a triangle can't be created."

class ZeroOrNegativeValueError(Exception):
    "Raised when a determined value is zero or negative."

class Polygon(ABC):
    """ This class was defined as an abstract class because it does not refer to any specific polygon """

    __slots__ = ['_sides']   # This setting prohibits new attributes from being created.

    def __init__(self, sides: List[float]) -> None:
        self._sides = sides
    
    def display_sides(self) -> List[float]:
        """ Returns a List[float] with the sides of the polygon """
        return self._sides

class Triangle(Polygon):
    __slots__ = ['_sides']   # This setting prohibits new attributes from being created.

    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
    
    def find_area(self) -> float:
        """ 
        This method uses the _sides attribute which contains a List[side: float (x3)] to calculate the area of a triangle.
        The calculation of the area is done using the Hero of Alexandria's Formula: A = square_root( p(p-a)(p-b)(p-c) ).
        Where A = area of the triangle, p = perimeter/2 and a, b and c = sides of the triangle.
        """
        [ a, b, c ] = self._sides
        p = sum([ a, b, c ]) / 2
        Area = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return Area

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

def validateTriangle(numTriangleSides: int) -> List[float]:
    """ This function gets the sides of the triangle and returns a list of the validated sides of the triangle """

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
    """ This is an initialization function that calculates the area of a triangle using classes and methods. """
    
    triangleSides = validateTriangle(3)
    triangle = Triangle(triangleSides)
    getTriangleSides = triangle.display_sides()
    getTriangleArea = triangle.find_area()

    print(f'\nLados do triângulo: {getTriangleSides}')
    print(f'\nÁrea do triângulo: {round(getTriangleArea, 3)}')

if __name__ == '__main__':
    main()