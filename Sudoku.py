import numpy as np


from tkinter import *


root = Tk()
root.title("Super Cool Super Slick Super Sudoku Solver")
#root.geometry("400x450")

"""
# add a title to the Sudoku board
visible_title = Label(root, text="Sudoku? Ha! Watch this!", font=("Arial", 30))
visible_title.grid(row=0, column=0, columnspan=3)

add_num = Entry(root, width=10)
add_num.grid(row=4, column=1, columnspan=3)

# create a function that updates the button text. I want to click, put a number and hit enter, done.
def updater(button):
    upd_num = add_num.get()
    button.config(text=upd_num)
    return
"""

# create the board

board = [[0,0,0,0,1,0,0,0,4],
         [5,0,4,8,0,0,9,7,0],
         [2,9,0,7,0,4,0,0,0],
         [1,0,0,4,2,0,0,6,0],
         [0,4,0,6,0,7,0,5,0],
         [0,7,0,0,3,5,0,0,8],
         [0,0,0,9,0,6,0,4,5],
         [0,8,9,0,0,2,3,0,7],
         [4,0,0,0,7,0,0,0,0]]


# publish the board to the screen
labels=[]
for row in board:
    for number in row:
        text = number
        label = Label(root, text=number)
        label.grid(row=row, column=number)
        labels.append(label)


print("Original Board: \n")
print(np.matrix(board))
print("\n\n")

def works(x, y, n):
    global board
    for i in range(0, 9):
        if board[i][x] == n:
            return False
    for i in range(0, 9):
        if board[y][i] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[y0+i][x0+j] == n:
                return False
    return True

def solver():
    global board
    for y in range(9):
         for x in range(9):
             if board[y][x] == 0:
                 for n in range(1, 10):
                     if works(x, y, n):
                         board[y][x] = n
                         solver()
                         board[y][x] = 0
                 return
    print("Solved Board: \n")
    print(np.matrix(board))
    input("More?\n")

solver()

"""
spot_11 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=1, column=0)
spot_12 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=1, column=1)
spot_13 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=1, column=2)
spot_21 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=2, column=0)
spot_22 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=2, column=1)
spot_23 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=2, column=2)
spot_31 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=3, column=0)
spot_32 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=3, column=1)
spot_33 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=3, column=2)

button_text11 = ""
button_text12 = ""
button_text13 = ""
button_text21 = ""
button_text22 = ""
button_text23 = ""
button_text31 = ""
button_text32 = ""
button_text33 = ""

but11 = Button(root, width=21, height=10, relief="flat", text="", command=lambda: updater(button_text11)).grid(row=1, column=0)
but12 = Button(root, width=21, height=10, relief="flat", text="", command=lambda: updater(button_text12)).grid(row=1, column=1)
but13 = Button(root, width=21, height=10, relief="flat", text="", command=lambda: updater(button_text13)).grid(row=1, column=2)
but21 = Button(root, width=21, height=10, relief="flat", text="", command=lambda: updater(button_text21)).grid(row=2, column=0)
but22 = Button(root, width=21, height=10, relief="flat", text="", command=lambda: updater(button_text22)).grid(row=2, column=1)
but23 = Button(root, width=21, height=10, relief="flat", text="", command=lambda: updater(button_text23)).grid(row=2, column=2)
but31 = Button(root, width=21, height=10, relief="flat", text="", command=lambda: updater(button_text31)).grid(row=3, column=0)
but32 = Button(root, width=21, height=10, relief="flat", text="", command=lambda: updater(button_text32)).grid(row=3, column=1)
but33 = Button(root, width=21, height=10, relief="flat", text="", command=lambda: updater(button_text33)).grid(row=3, column=2)


# Need to build a function that updates the button text. See link here:
# https://stackoverflow.com/questions/32615440/python-3-tkinter-how-to-update-button-text/53201471

"""
root.mainloop()