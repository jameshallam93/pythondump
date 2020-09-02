import pandas as pd

data = pd.ExcelFile("C:/Users/Mushroom/python/python/barstaff.xlsx")

dataframe = pd.read_excel(data)
bar_list = []

class Bartender:
    def __init__(self, name, title, wage, experience):
        self.name = name
        self.title = title
        self.wage = wage
        self.experience = experience



def add_all_barstaff():
    for i in dataframe.index:
        name = dataframe.iat[i, 0]
        title = dataframe.iat[i, 1]
        wage = dataframe.iat[i, 2]
        experience = dataframe.iat[i, 3]

        bartender = Bartender(name, title, wage, experience)
        bar_list.append(bartender)
        
add_all_barstaff()

print(len(bar_list))
print(bar_list[0].name)

        





    
