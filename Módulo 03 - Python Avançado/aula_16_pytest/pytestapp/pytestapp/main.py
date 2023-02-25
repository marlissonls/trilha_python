import requests, json
 
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

        content_json.append({"id": len(content_json) + 1, "advice": self._advice})

        with open("advices/advices.json", "w") as advice_file:
            advice_file.write(json.dumps(content_json))

    @classmethod
    def show_old_advices(cls) -> list:
        """ Returns a list of old advices from json file """

        with open("advices/advices.json", "r") as advice_file:
            return json.loads(advice_file.read())

def main():
    """ 
    Requests a new advice from Advice class and prints it;
    Writes the advice on a json file; and
    Gets all recorded advices from the json file and prints it's content.
    """

    advice = Advice()
    print(advice, end="\n\n")

    advice.write_advice()
    
    print(Advice.show_old_advices())

if __name__ == '__main__':
    main()