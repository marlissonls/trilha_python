import requests
import os
import datetime
 
class Advice:
    __slots__ = ['_advice']
    def __init__(self) -> None:
        self._advice = requests.get("https://api.adviceslip.com/advice", {"Accept": "application/json"}).json()['slip']['advice']
    
    def __str__(self) -> str:
        return self._advice
    
    def write_advice(self) -> None:
        with open("advices/advices.txt", "a") as advice_file:
            advice_file.write(f"\n\n{datetime.datetime.now()} \n")
            advice_file.write(self._advice)
    
    def show_old_advices(self) -> str:
        with open("advices/advices.txt", "r+") as advice_file:
            return advice_file.read()

def main():
    advice = Advice()
    print(advice)
    advice.write_advice()
    print(advice.show_old_advices())

if __name__ == '__main__':
    main()