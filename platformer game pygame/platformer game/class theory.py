from tkinter import *

root = Tk()




class Persona:

    def __init__(self, generation, energy, wisdom, charisma):
        self.generation = generation
        self.energy = energy
        self.wisdom = wisdom
        self.charisma = charisma

#millenial = Persona("millenial", 10, 3, 5)

class_label = Label(root, text = "Choose a persona")
class_label.grid(rowspan = 2)

def choose_millen():
    global char_class
    char_class = Persona("Millenial", 10, 3, 5)

def choose_boomer():
    global char_class
    char_class = Persona("Boomer", 4, 6, 3)

def choose_greatest():
    global char_class
    char_class = Persona("Greatest", 1, 10, 9)
    
millenial_button = Button(root, text = "Millenial", command = choose_millen)
millenial_button.grid(row = 1, column = 1)

boomer_button = Button(root, text = "Booemr", command = choose_boomer)
boomer_button.grid(row = 1, column = 2)

greatest_button = Button(root, text = "Greatest generation", command = choose_greatest)
greatest_button.grid(row = 1, column = 3)

def print_stats():
    print("""You are part of the %s generation
Your energy level is %s
Your wisdom is %s
Your charisma is %s""" %(char_class.generation, char_class.energy, char_class.wisdom, char_class.charisma))

stats_button = Button(root, text = "print stats", command = print_stats)
stats_button.grid(row = 2, column = 2)



root.mainloop()

