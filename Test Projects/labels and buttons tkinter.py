from tkinter import *

root = Tk()

# label is used to add text in the format x = Label(object, text = "add text here")
#bg means the background colour
#fg refers to foreground colour
#same for buttons and other widgets


#the_label = Label(root, text="This is my first label", bg = "white")
#.pack() is used to literally pack widgets into the screen in whatever way works
#the_label.pack()


#label_the2nd = Label(root, text = "New label", bg = "orange")

#pack(fill = (XY)) will make the label fill the whole X/Y axis

#label_the2nd.pack(fill = X)


#the_label.pack()
#frames are used to divide the window up - must be more than one
#top_frame = Frame(root)
#top_frame.pack()

#bottom_frame = Frame(root)
#pack(side = ***) instructs the CPU where to place the frame
#bottom_frame.pack(side=BOTTOM)

#buttons can be created using the Button(frame, text = ** fg = "choose a colour")


#button1 = Button(top_frame, text = "1st button", fg="red")
#button2 = Button(top_frame, text = "2nd button", fg = "blue")
#button3 = Button(top_frame, text = "3rd button", fg = "orange")
#button4 = Button(bottom_frame, text = "4th button", fg = "purple")

#to have buttons appear on the screen, they still need to be packed
#button.pack(side = (eg. LEFT, RIGHT, BOTTOM))
#be aware that buttons will be packed in order, so button2 will be to the right of button1 etc.


#button1.pack(side = LEFT)
#button2.pack(side = LEFT)
#button3.pack()
#button4.pack(side = BOTTOM)


label_X = Label(root, text = "Name:")
label_Y = Label(root, text = "Password:")

entry1 = Entry(root)
entry2 = Entry(root)

#grid is an alternative() to pack(), which creates a grid with an arbitrary no.of rows/columns
# if not specified, the rows and columns will default to 0
#sticky alligns the widget within its position on the page, and uses NESW instead of LRUP
#the labels below have been alligned to the RHS

label_X.grid(row = 0, sticky = E)
label_Y.grid(row = 1, sticky = E)
entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)

#checkboxes can be created using the Checkbutton(object, text = "***")
#to make a widget span over multiple rows and columns, you can use columnspan/rowspan
# and choose the number of "cells" it spans over

checkbox = Checkbutton(root, text = "Stay logged in?")
checkbox.grid(columnspan = 2)


def print_name():
    print("hello, my name is James")

#one way of binding functions to buttons is to use the "command" option within the button setup
#in the format command = function_name - do not include the parentheses at the end of the function

button_name = Button(root, text = "Print your own name", command = print_name)
button_name.grid(row = 3, columnspan = 2)
    
def print_different_name(event):
    print("another name is Thomas")
def print_second(event):
    print("Un autre nom est Stephane")
def print_third(event):
    print("Un nombre finale es Theo")
#.bind("<Button-x>", function_name) can also be used to bind a function to a button
# in this case, x can be replaced with 1, 2 or 3 to assign each of the mouse clicks to a different function

button_other = Button(root, text = "print a different name", )
button_other.bind("<Button-1>", print_different_name)
button_other.bind("<Button-2>", print_second)
button_other.bind("<Button-3>", print_third)

button_other.grid(row = 4, columnspan = 2)

#mainloop() loops the object so that it remains on the screen instead of running once and stopping
root.mainloop()


