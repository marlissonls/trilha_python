import requests
import json
 
class Advice:
    __slots__ = ['_advice']
    def __init__(self) -> None:
        """ Builds a new instance of the Advice class assigning a new advice from a advice api. """
        self._advice = requests.get("https://api.adviceslip.com/advice", {"Accept": "application/json"}).json()['slip']['advice']
    
    def __str__(self) -> str:
        """ Returns the _advice attribute. """
        return self._advice
    
    def write_advice(self) -> None:
        """ Gets data from a json file, appends a new content to it and rewrite the json file with the modified data. """

        with open("advices/advices.json", "r") as advice_file:
            content_json = json.loads(advice_file.read())

        content_json.append(json.dumps({"id": len(content_json) + 1, "advice": self._advice}))

        with open("advices/advices.json", "w") as advice_file:
            advice_file.write(json.dumps(content_json))

    @classmethod
    def show_old_advices(cls) -> list:
        """ Returns a list of old advices from json file """

        list_of_dicts = []
        with open("advices/advices.json", "r") as advice_file:
            content_json = json.loads(advice_file.read())

        for dictionay in content_json:
            list_of_dicts.append(json.loads(dictionay))

        return list_of_dicts

def main():
    advice = Advice()
    print(advice)
    advice.write_advice()
    print(Advice.show_old_advices())

if __name__ == '__main__':
    main()