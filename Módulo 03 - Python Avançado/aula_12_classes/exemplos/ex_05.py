class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def	__repr__(self):
        return "Ponto({}, {})".format(self.x + 1, self.y + 1)

if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = eval(repr(p1))
    print(p1)
    print(p2)

# __str__ vs __repr__
# __add__(), __mul__() , __div__(), __mod__() e __pow__()	