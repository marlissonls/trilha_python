import pandas as pd
from typing import List

class DisplayData:
    def __init__(self):
        self.id_list = []
        self.first_name_list = []
        self.last_name_list = []
        self.email_list = []

    def to_fill_columns(self, result: List[tuple]):
        for client in result:
            self.id_list.append(client[0])
            self.first_name_list.append(client[1])
            self.last_name_list.append(client[2])
            self.email_list.append(client[3])
    
    def to_empty_columns(self):
        self.__init__()

    def generate_table(self, result: List[tuple]):
        self.to_fill_columns(result)
        result_table = pd.DataFrame({
            'ID|': self.id_list,
            'FIRST NAME|': self.first_name_list,
            'LAST NAME|': self.last_name_list,
            'EMAIL|': self.email_list
        })
        self.to_empty_columns()
        print('\n')
        print(result_table)
        