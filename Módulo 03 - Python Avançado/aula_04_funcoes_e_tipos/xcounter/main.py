from typing import List

def get_user_words() -> List[str]:
    """ 
    This is a pure function that takes a sentence and splits it into a List of words.
    """
    words = input('Escreva uma frase: ').split()
    return words

def count_x_occurrences(word: str) -> int:
    """
    This is a pure function that takes a word and counts the occurrences of the letter 'x' in it.
    """
    counter = 0
    for i in word:
        if i == 'x' or i == 'X':
            counter += 1
    return counter

def inform_average(average: float) -> None:
    """
    This is a pure function that takes the average of occurrences of 'x' and prints it out.
    """
    print('A média de ocorrência de letras X é %.2f' %average)


words = get_user_words()
fullSize = 0
xCounter = 0

for word in words:
    fullSize += len(word)
    xCounter += count_x_occurrences(word)

average = xCounter/fullSize
inform_average(average)