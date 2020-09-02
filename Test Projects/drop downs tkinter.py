from tkinter import *

def do_nothing():
    print("Nothing")
def do_something():
    print("Something")
def everythang():
    print("will be alright")
    
root = Tk()

drop = Menu(root)
root.config(menu=drop)

sub_drop = Menu(drop)
drop.add_cascade(label = "File", menu = sub_drop)
sub_drop.add_command(label = "New project", command = do_nothing)
sub_drop.add_command(label = "Test", command = do_something)
sub_drop.add_separator()
sub_drop.add_command(label = "Everythang", command = everythang)

sub_drop2 = Menu(drop)
drop.add_cascade(label = "Edit", menu = sub_drop2)
sub_drop2.add_command(label = "Newer project", command = do_nothing)


root.mainloop()

