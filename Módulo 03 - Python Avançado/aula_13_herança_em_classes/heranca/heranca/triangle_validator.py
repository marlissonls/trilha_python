from customized_errors import TriangleError
from polygon_sides_validator import validateSides
from typing import List

def validateTriangle(numTriangleSides: int) -> List[float]:
    """ This function gets the sides of the triangle and returns a list of the validated sides of the triangle """

    while True:
        try:
            [ a, b, c ] = validateSides(numTriangleSides, 'triângulo')
            
            boolean_1 = a + b <= c
            boolean_2 = a + c <= b
            boolean_3 = b + c <= a

            if boolean_1 or boolean_2 or boolean_3:
                raise TriangleError
            
        except TriangleError:
            print('\nTriangleError: Os lados informados não podem formar um triâgulo!')
            print('Motivo: O tamanho de um dos lados é igual ou superior à soma dos tamanhos dos outros dois lados.')
        else:
            return [ a, b, c ]