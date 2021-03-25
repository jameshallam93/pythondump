import tkinter as tk
from tkinter import ttk
import math
#look into partial vs lambda
from functools import partial
import random as rd
import time as time

#Font packages
LARGE_FONT = ("Carto Gothic", 16, "bold")
MED_FONT  = ("Carto Gothic", 12, "bold")



# controller class - need to understand how this works
class app_windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default = "icon.ico")
        #contains all the frames
        container = tk.Frame(self)
        self.geometry("500x500")
        #stops the screen from being resized
        self.resizable(0, 0)
        self.title("HUI")
        container.pack(side = "top", fill = "both", expand = True)
        #sets the grid parameters for all the rest of the pages
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        #very important - creates the list of webpages that can be accessed by 
        for F in (splash_frame, ttt_page, XXXX, tkinter_games, basic, web_scrape, start_page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(splash_frame)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    

    
class splash_frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        width = 500
        height = 500
        canvas = tk.Canvas(self, width = 500, height = 500)
    
        logo = tk.PhotoImage(file = "true_logo.gif")
        self.logo = logo
        canvas.create_image(250, 250, image = logo)
        canvas.pack()
        self.lift()
        self.after(1000, self.destroy)

class start_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        frame_bg = tk.PhotoImage(file = "bg_image.gif")
        frame_bg.image = frame_bg

        rows = 0
        while rows < 10:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows,weight=1)
            rows += 1
        
        bg_label = tk.Label(self, image = frame_bg)
        bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        title_canvas = tk.Canvas(self, width = 350, height = 50, bg = "black")
        title_canvas.grid(row = 1, column = 2, columnspan = 6)
        title_canvas.create_text(175, 28, text = "Welcome to Hooeee - Hallam's GUI", font = LARGE_FONT, fill = "white")

        apps_canvas = tk.Canvas(self, width = 175, height = 50, bg = "black")
        apps_canvas.grid(row = 3, column = 2, columnspan = 3)
        apps_canvas.create_text(88, 25, text = "Apps", font = MED_FONT, fill = "white")

        games_canvas = tk.Canvas(self, width = 175, height = 50, bg = "black")
        games_canvas.grid(row = 3, column = 5, columnspan = 3)
        games_canvas.create_text(88, 25, text = "Games", font = MED_FONT, fill = "white")

        apps_menu_can = tk.Canvas(self, width = 200, height = 300, bg = "black")
        apps_menu_can.grid(row = 5, column = 2, columnspan = 3)

        scrape_button = tk.Button(self, text = "Web Scraping", font = MED_FONT, fg = "white", bg = "black", command = lambda: controller.show_frame(web_scrape))
        scrape_button.configure(width = 17, height = 2)
        scrape_button_window = apps_menu_can.create_window(12, 12, window = scrape_button, anchor = "nw")

        basic_button = tk.Button(self, text = "Basic Scripts", font = MED_FONT, fg = "white", bg = "black", command = lambda: controller.show_frame(basic))
        basic_button.configure(width = 17, height = 2)
        basic_button_window = apps_menu_can.create_window(12, 74, window = basic_button, anchor = "nw")
        #to fill XXXX in with (i.e. business progs, web applications)
        xxxx_button = tk.Button(self, text = "XXXX", font = MED_FONT, bg = "black", fg = "white", command = lambda: controller.show_frame(XXXX))
        xxxx_button.configure(width = 17, height = 2)
        xxx_button_window = apps_menu_can.create_window(12, 136, window = xxxx_button, anchor = "nw")
        xxxx1_button = tk.Button(self, text = "XXXX", font = MED_FONT, bg = "black", fg = "white", command = lambda: controller.show_frame(XXXX))
        xxxx1_button.configure(width = 17, height = 2)
        xxx1_button_window = apps_menu_can.create_window(12, 192, window = xxxx1_button, anchor = "nw")

        games_menu_can = tk.Canvas(self, width = 200, height = 300, bg = "black")
        games_menu_can.grid(row = 5, column = 5, columnspan = 3)

        tk_game_button = tk.Button(self, text = "Tkinter", font = MED_FONT, fg = "white", bg = "black", command =lambda: controller.show_frame(tkinter_games))
        tk_game_button.configure(width = 17, height = 2)
        tk_game_button_window = games_menu_can.create_window(12, 12, window = tk_game_button, anchor = "nw")

        py_game_button = tk.Button(self, text = "Pygame", font = MED_FONT, fg = "white", bg = "black", command = lambda: controller.show_frame(pg_games))
        py_game_button.configure(width = 17, height = 2)
        py_game_button_window = games_menu_can.create_window(12, 74, window = py_game_button, anchor = "nw")

        xxxx2_button = tk.Button(self, text = "XXXX", font = MED_FONT, bg = "black", fg = "white", command = lambda: controller.show_frame(XXXX))
        xxxx2_button.configure(width = 17, height = 2)
        xxx2_button_window = games_menu_can.create_window(12, 136, window = xxxx2_button, anchor = "nw")
        xxxx3_button = tk.Button(self, text = "XXXX", font = MED_FONT, bg = "black", fg = "white", command = lambda: controller.show_frame(XXXX))
        xxxx3_button.configure(width = 17, height = 2)
        xxx3_button_window = games_menu_can.create_window(12, 192, window = xxxx3_button, anchor = "nw")
        
        """apps_label = tk.Label(self, text = "Apps")"""

        
class web_scrape(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Web scraping programs", font =LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        np_button = tk.Button(self, text = "home", command =lambda: controller.show_frame(start_page))
        np_button.pack()


class basic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Basic Scripts", font =LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        np_button = tk.Button(self, text = "home", command =lambda: controller.show_frame(start_page))
        np_button.pack()

class XXXX(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = " test screen", font =LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        np_button = tk.Button(self, text = "home", command =lambda: controller.show_frame(start_page))
        np_button.pack()

class tkinter_games(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        frame_bg = tk.PhotoImage(file = "bg_image.gif")
        frame_bg.image = frame_bg

        rows = 0
        while rows < 10:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows,weight=1)
            rows += 1
        
        bg_label = tk.Label(self, image = frame_bg)
        bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        title_canvas = tk.Canvas(self, width = 350, height = 50, bg = "black")
        title_canvas.grid(row = 1, column = 2, columnspan = 6)
        title_canvas.create_text(175, 28, text = "Tkinter Games", font = LARGE_FONT, fill = "white")

        apps_canvas = tk.Canvas(self, width = 175, height = 50, bg = "black")
        apps_canvas.grid(row = 3, column = 2, columnspan = 3)
        apps_canvas.create_text(88, 25, text = "Game", font = MED_FONT, fill = "white")

        games_canvas = tk.Canvas(self, width = 175, height = 50, bg = "black")
        games_canvas.grid(row = 3, column = 5, columnspan = 3)
        games_canvas.create_text(88, 25, text = "Description", font = MED_FONT, fill = "white")

        apps_menu_can = tk.Canvas(self, width = 200, height = 300, bg = "black")
        apps_menu_can.grid(row = 5, column = 2, columnspan = 3)

        ttt_game_button = tk.Button(self, text = "Tic Tac Toe", font = MED_FONT, fg = "white", bg = "black", command =lambda: controller.show_frame(ttt_page))
        ttt_game_button.configure(width = 17, height = 2)
        ttt_game_button_window = apps_menu_can.create_window(12, 12, window = ttt_game_button, anchor = "nw")

class pg_games(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Pygame Games", font =LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        np_button = tk.Button(self, text = "home", command =lambda: controller.show_frame(start_page))
        np_button.pack()



class ttt_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        rows = 0
        while rows < 10:
            self.rowconfigure(rows, weight=0)
            self.columnconfigure(rows,weight=0)
            rows += 1

        self.grid_columnconfigure(1, minsize=100)
        self.grid_rowconfigure(1, minsize = 100)
        board_positions = ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"]
        #to store the buttons separate to board positions for use in cpu_turn()
        button_idents = []
        
        board_canvas = tk.Canvas(self, width = 300, height = 300, bg = "white")
        board_canvas.grid(row = 3, column = 3)  

        """test_button = tk.Button(self, text = " ", height = 6, width = 13)
        test_button_window = board_canvas.create_window(2, 2, window = test_button, anchor = "nw")
        test_button2 = tk.Button(self, text = " ", height = 6, width = 13)
        test_button2_window = board_canvas.create_window(102, 102, window = test_button2, anchor = "nw")
        test_button3 = tk.Button(self, text = " ", height = 6, width = 13)
        test_button3_window = board_canvas.create_window(202, 202, window = test_button3, anchor = "nw")"""                
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
            x_value = 2
            y_value = 0
            x = 1
            #for loop to create all the buttons
            for i in board_positions:
                

                
                b_i = tk.Button(self, text = i, height = 5, width = 10)
                b_i.configure(command = partial(change_user, b_i))
                button_idents.append(b_i)

                if (x-1)%3 == 0:
                    y_value +50
                if(x_value - 2)/100 == 3:
                    x_value -= 150
                if x/ 3 <=1:
                    b_i_window = board_canvas.create_window(x_value, y_value, window = b_i, anchor = "nw")
                    x_value +=100
                    x+=1
                if x/3 <=2:
                    b_i_window = board_canvas.create_window(x_value, y_value, window = b_i, anchor = "nw")
                    x_value +=100
                    x += 1
                else:
                    b_i_window = board_canvas.create_window(x_value, y_value, window = b_i, anchor = "nw")
                    x_value +=100
                    x += 1
                """b_i = tk.Button(self, text = " ", width = 4, height = 2)
                b_i_window = board_canvas.create_window(0, 0, window = ttt_game_button, anchor = "nw")
                b_i.configure(command = partial(change_user, b_i))
                button_idents.append(b_i)
                if x / 3 <= 1:
                    b_i.grid(row = 4, column = col_value)
                    b_i.configure(height = 2, width = 4)
                    col_value += 1
                    x += 1
                elif x / 3 > 1 and x / 3 <= 2:
                    if col_value == 3:
                        col_value = 0
                    b_i.grid(row = 5, column = col_value)
                    col_value += 1
                    x += 1
                else:
                    if col_value == 3:
                        col_value = 0
                    b_i.grid(row = 6, column = col_value)
                    col_value += 1
                    x += 1
            restart_button = tk.Button(self, text = "Restart?", command = restart)
            restart_button.grid(row = 3, column = 3)
            back_button = tk.Button(self, text = "back to home screen?", command = lambda: controller.show_frame(start_page))
            back_button.grid(row = 3, column = 4)"""
            





        draw_board()

                


            

        

app = app_windows()
app.mainloop()

        
    
        
            

