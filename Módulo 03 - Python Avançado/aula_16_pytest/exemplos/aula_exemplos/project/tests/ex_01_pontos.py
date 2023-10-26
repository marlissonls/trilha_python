from dataclasses import dataclass
import unittest

@dataclass
class Point:
    x: int
    y: int

    def __add__(self, p: "Point") -> "Point":
        return Point(self.x + p.x, self.y + p.y)

class TestPoints(unittest.TestCase):
    def test_soma_com_positivo(arg) -> None:
        """
        The arg parameter only prevents the error: 
        ERROR: test_soma_com_positivo (__main__.TestPoints), where "__main__.TestPoints" is send as argument.
        TypeError: TestPoints.test_soma_com_positivo() takes 0 positional arguments but 1 was given
        """
        
        a = Point(5, 7)
        b = Point(1, 10)
        result = a + b
        expected_result = Point(6, 17)
        assert result == expected_result

    def test_soma_com_negativo(arg) -> None:
        """
        The arg parameter only prevents the error: 
        ERROR: test_soma_com_negativo (__main__.TestPoints), where "__main__.TestPoints" is send as argument.
        TypeError: TestPoints.test_soma_com_positivo() takes 0 positional arguments but 1 was given
        """
        a = Point(5, 7)
        b = Point(-1, -10)
        result = a + b
        expected_result = Point(4, -3)
        assert result == expected_result

if __name__ == '__main__':
    unittest.main()