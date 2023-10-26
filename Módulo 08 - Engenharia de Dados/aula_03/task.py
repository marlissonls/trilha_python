import pandas as pd

class Data:
    def __init__(self):
        self.name_list = []
        self.age_list = []
        self.data_table = None

    def fill_columns(self, people):
        for person in range(people):
            name = input(f"\nInsira o nome da {person + 1}ª pessoa: ")
            self.name_list.append(name)

            age = int(input(f"\nInsira a idade da {person + 1}ª pessoa: "))
            self.age_list.append(age)
    
    def empty_columns(self):
        self.__init__()

    def generate_table(self):
        people = int(input("\nInsira a quantidade de pessoas: "))
        self.fill_columns(people)
        self.data_table = pd.DataFrame({
            "NOME": self.name_list,
            "IDADE": self.age_list
        })
        self.display_data()
        self.empty_columns()

    def display_data(self):
        print("\n", self.data_table)
        print("\nMédia das idades: ", self.data_table["IDADE"].mean())

if __name__ == "__main__":
    dados = Data()
    dados.generate_table()