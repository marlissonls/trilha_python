from typing import Generator

def fibonacci(limit: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    while b < limit:
        a, b = b,  a + b
        yield a
    
    for n in fibonacci(20):
        print(n)