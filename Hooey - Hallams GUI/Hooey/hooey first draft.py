import tkinter as tk
import math
from functools import partial
import random as rd
import time as time


LARGE_FONT = ("Comic Sans", 12)

class app_windows(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (start_page, page_one, page_two, ttt_page):
        
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(start_page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


    


class start_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "This is a test label", font =LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        np_button = tk.Button(self, text = "next page", command =lambda: controller.show_frame(page_one))
        np_button.pack()

        np_button = tk.Button(self, text = "page two", command =lambda: controller.show_frame(page_two))
        np_button.pack()

        np_button = tk.Button(self, text = "Tic Tac Toe", command =lambda: controller.show_frame(ttt_page))
        np_button.pack()
        
class page_one(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "This is a second test label", font =LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        np_button = tk.Button(self, text = "home", command =lambda: controller.show_frame(start_page))
        np_button.pack()

        np_button = tk.Button(self, text = "page two", command =lambda: controller.show_frame(page_two))
        np_button.pack()


class page_two(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Third test", font =LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        np_button = tk.Button(self, text = "home", command =lambda: controller.show_frame(start_page))
        np_button.pack()

        np_button = tk.Button(self, text = "page one", command =lambda: controller.show_frame(page_one))
        np_button.pack()

class ttt_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        board_positions = ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"]
        #to store the buttons separate to board positions for use in cpu_turn()
        button_idents = []



        """def is_draw():
            for ident in (button_idents["text"]):
                if ident == False:
                    return False
                else:
                    return True"""

        def is_draw():
            for ident in (button_idents):
                if ident["text"] == " ":
                    return False

        def is_win_user():
            if ((button_idents[0]["text"] == "X" and button_idents[1]["text"] == "X" and button_idents[2]["text"] == "X") or
            (button_idents[3]["text"] == "X" and button_idents[4]["text"] == "X" and button_idents[5]["text"] == "X") or
            (button_idents[6]["text"] == "X" and button_idents[7]["text"] == "X" and button_idents[8]["text"] == "X") or
            (button_idents[0]["text"] == "X" and button_idents[3]["text"] == "X" and button_idents[6]["text"] == "X") or
            (button_idents[1]["text"] == "X" and button_idents[4]["text"] == "X" and button_idents[7]["text"] == "X") or
            (button_idents[2]["text"] == "X" and button_idents[5]["text"] == "X" and button_idents[8]["text"] == "X") or
            (button_idents[0]["text"] == "X" and button_idents[4]["text"] == "X" and button_idents[8]["text"] == "X") or
            (button_idents[2]["text"] == "X" and button_idents[4]["text"] == "X" and button_idents[6]["text"] == "X")):
                print("winner!")
                time.sleep(3)
                restart()


        def is_win_cpu():
            if ((button_idents[0]["text"] == "O" and button_idents[1]["text"] == "O" and button_idents[2]["text"] == "O") or
            (button_idents[3]["text"] == "O" and button_idents[4]["text"] == "O" and button_idents[5]["text"] == "O") or
            (button_idents[6]["text"] == "O" and button_idents[7]["text"] == "O" and button_idents[8]["text"] == "O") or
            (button_idents[0]["text"] == "O" and button_idents[3]["text"] == "O" and button_idents[6]["text"] == "O") or
            (button_idents[1]["text"] == "O" and button_idents[4]["text"] == "O" and button_idents[7]["text"] == "O") or
            (button_idents[2]["text"] == "O" and button_idents[5]["text"] == "O" and button_idents[8]["text"] == "O") or
            (button_idents[0]["text"] == "O" and button_idents[4]["text"] == "O" and button_idents[8]["text"] == "O") or
            (button_idents[2]["text"] == "O" and button_idents[4]["text"] == "O" and button_idents[6]["text"] == "O")):
                print("Computer wins!")
                time.sleep(3)
                restart()

        def cpu_turn():
            is_win_user()
            choice = rd.randint(0, 8)
            cpu_choice = button_idents[choice]
            if cpu_choice["text"].isspace():
                change_cpu(cpu_choice)
            else:
                cpu_turn()

        def change_cpu(randchoice):
            randchoice.configure(text = "O")
            is_win_cpu()


        def change_user(n):
            #while n["text"] != "X":
                if n["text"] == " ":
                    n.configure(text = "X")
                elif n["text"] == "O":
                    print("That square is taken by the opponent")
                    return
                elif n["text"] == "X":
                    print("You have already taken that square, opponents turn")
                    return
                cpu_turn()

        # redraw the board to restart game
        def restart():
            for button in button_idents:
                button.destroy()
            button_idents.clear()
            draw_board()

        #set up a new board with blank buttons
        def draw_board():
            for button in (button_idents):
                button.destroy()
            col_value = 0
            x = 1
            #for loop to create all the buttons
            for i in board_positions:
                b_i = tk.Button(self, text = " ", width = 4, height = 2)
                b_i.configure(command = partial(change_user, b_i))
                button_idents.append(b_i)
                if x / 3 <= 1:
                    b_i.grid(row = 0, column = col_value)
                    col_value += 1
                    x += 1
                elif x / 3 > 1 and x / 3 <= 2:
                    if col_value == 3:
                        col_value = 0
                    b_i.grid(row = 1, column = col_value)
                    col_value += 1
                    x += 1
                else:
                    if col_value == 3:
                        col_value = 0
                    b_i.grid(row = 2, column = col_value)
                    col_value += 1
                    x += 1
            restart_button = tk.Button(self, text = "Restart?", command = restart)
            restart_button.grid(row = 3, column = 3)
            back_button = tk.Button(self, text = "back to home screen?", command = lambda: controller.show_frame(start_page))
            back_button.grid(row = 3, column = 4)
            





        draw_board()

                


            

        

app = app_windows()
app.mainloop()

        
    
        
            

