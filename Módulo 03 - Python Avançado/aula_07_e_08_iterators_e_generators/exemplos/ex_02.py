class Fibonacci:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.a = 0
        self.b = 1
    
    def __next__(self) -> int:
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.limit:
            raise StopIteration
        return self.a

x = Fibonacci(20)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

for n in Fibonacci(20):
    print(n)