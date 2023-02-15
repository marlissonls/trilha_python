""" 
Crie a classe Polygon com um construtor que recebe “sides: List[float]” e um método “display_sides() -> List[float]”.
Crie também a classe Triangle que herda o Polygon e implementa o “find_area() -> float”.
"""
from abc import ABC
from typing import List
import math


class Polygon(ABC):
    def __init__(self, sides: List[float]) -> None:
        self._sides = sides
    
    def display_sides(self) -> List[float]:
        """ Retorna uma lista do float os lados do polígono """
        return self._sides

class Triangle(Polygon):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
    
    def find_area(self) -> float:
        """ 
        Calculo da área usando a Fórmula de Herão de Alexandria: A = [p(p-a)(p-b)(p-c)]^(0.5)
        em que A = área do triângulo, p = perímetro/2 e a, b e c = lados do triângulo.
        """
        a, b, c = self._sides[0], self._sides[1], self._sides[2]
        p = 0.5 * (a + b + c)
        A = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return A

def main() -> None:
    """
    Esta função pede os lados de um triângulo, cria uma instância de um Triangle, 
    mostra uma lista com os lados do triângulo e mostra o valor da área do triângulo
    """
    poli = Polygon([2.1,2.3])
    print(poli.display_sides())
    
    sides = [float(i) for i in input('Informe 3 números separados por espaços: ').split()]
    triangulo = Triangle(sides)
    print(f'\nLados do triângulo: {triangulo.display_sides()}')
    print(f'\nÁrea do triângulo: {triangulo.find_area()}')

if __name__ == '__main__':
    main()