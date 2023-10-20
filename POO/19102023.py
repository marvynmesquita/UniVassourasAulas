import pandas as pd
from abc import ABC, abstractmethod

class PandaPublisher:
    def __init__(self):
        self.data = pd.DataFrame();

    def add_data(self, data_dict):
        if not isinstance(data_dict, dict):
            raise TypeError('data_dict must be a dict')
        new_data = pd.DataFrame(data_dict)
        self.data = pd.concat([self.data, new_data], ignore_index=True)

    def display_data(self):
        print(self.data)

df = PandaPublisher()

data1 = {'Nome': ['João', 'Maria', 'José', 'Pedro'], 'Idade': [20, 19, 18, 21]}
data2 = {'Nome': ['Ana', 'Paula', 'Carla', 'Mariana'], 'Idade': [22, 23, 24, 25]}

df.add_data(data1)
df.add_data(data2)

df.display_data()