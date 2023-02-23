""" 
Crie a classe Polygon com um construtor que recebe “sides: List[float]” e um método “display_sides() -> List[float]”.
Crie também a classe Triangle que herda o Polygon e implementa o “find_area() -> float”.
"""

from abc import ABC
from typing import List
import math
from triangle_validator import validateTriangle

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