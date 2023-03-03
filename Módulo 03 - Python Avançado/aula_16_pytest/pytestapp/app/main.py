from requests import get as http_get_request
from os.path import dirname as package_directory, realpath as this_module_path
from json import loads as change_type_to_json, dumps as change_type_to_str

class Advice:
    __slots__ = ['_advice']   # attributes limitator
    
    # attributes for http requests
    _api_url: str = "https://api.adviceslip.com/advice"
    _api_headers: dict = {"Accept": "application/json"}
    _api_request_fail_msg: str = "Advice API request error."

    # attributes for file handling
    _json_advice_file_path: str = f"{package_directory(this_module_path(__file__))}/advices/advices.json"
    _write_advice_success_msg: str = "The advice was written to the file succesfully!"
    _write_advice_fail_msg: str = "Something went wrong! The advice wasn't written to the file."
    _show_old_advices_fail_msg: str = "Something went wrong! The file cannot be read."

    def __init__(self) -> None:
        """ Builds a new instance of the Advice class assigning a new advice from a advice api. """

        try:
            self._advice: str = http_get_request(Advice._api_url, Advice._api_headers).json()['slip']['advice']
        except Exception:
            print(Advice._api_request_fail_msg)
    
    def __str__(self) -> str:
        """ Returns the _advice attribute. """
        return self._advice
    
    def write_advice(self) -> str:
        """ Gets a list from a json file, appends a new advice to it and rewrite the json file with the modified list. """

        try:
            with open(Advice._json_advice_file_path, "r") as advice_file:
                json_content: list = change_type_to_json(advice_file.read())

            json_content.append({"id": len(json_content) + 1, "advice": self._advice})

            with open(Advice._json_advice_file_path, "w") as advice_file:
                advice_file.write(change_type_to_str(json_content))
        except Exception: 
            return Advice._write_advice_fail_msg
        else:
            return Advice._write_advice_success_msg

    @classmethod
    def show_old_advices(cls) -> list | str:
        """ Shows a list of old advice from the json file """

        try:
            with open(Advice._json_advice_file_path, "r") as advice_file:
                json_content: list = change_type_to_json(advice_file.read())
        except Exception:
            return Advice._show_old_advices_fail_msg
        else:
            return json_content

def main() -> None:
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