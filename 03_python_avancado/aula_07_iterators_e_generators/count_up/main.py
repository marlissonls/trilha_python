from typing import Generator

def count_up(x_limit: int) -> Generator[int, None, None]:
    """
    This function takes a limit number and returns a Generator that returns the numbers less than the limit number.
    where the difference of one term of the sequence to the previous one increases by one.
    """
    # Initializing elements.
    x = 1
    iterator = 1

    while x < x_limit:
        # Returns the value of current element.
        yield x

        # Updates the variables to calc the next element.
        x = x + iterator
        iterator += 1

if __name__ == '__main__':
    # Cria um generator de números onde a diferença de um termo da sequência para o anterior aumenta em uma unidade
    x_limit = int(input("Informe o número x limite da sequência: "))
    count_up_limit = count_up(x_limit)

    for counting_number in count_up_limit:
        print(counting_number)