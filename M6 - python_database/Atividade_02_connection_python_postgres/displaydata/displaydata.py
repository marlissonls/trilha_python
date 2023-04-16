import pandas as pd
from typing import List

class DisplayData:
    def __init__(self):
        self.id_column = []
        self.first_name_column = []
        self.last_name_column = []
        self.email_column = []

    def to_fill_columns(self, result: List[tuple]):
        for client in result:
            self.id_column.append(client[0])
            self.first_name_column.append(client[1])
            self.last_name_column.append(client[2])
            self.email_column.append(client[3])
    
    def to_empty_columns(self):
        self.__init__()

    def generate_table(self, result: List[tuple]):
        self.to_fill_columns(result)
        result_table = pd.DataFrame({
            '     ID': self.id_column,
            '       FIRST NAME': self.first_name_column,
            '       LAST NAME': self.last_name_column,
            '                    EMAIL': self.email_column
        })
        self.to_empty_columns()
        print('\n')
        print(result_table)
        