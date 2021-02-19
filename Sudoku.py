from tkinter import *

root = Tk()
root.title("Super Cool Super Slick Super Sudoku Solver")
#root.geometry("400x450")

# add a title to the Sudoku board
visible_title = Label(root, text="Sudoku? Easy Peasey", font=("Arial", 30))
visible_title.grid(row=0, column=0, columnspan=3)

# create a function that updates one of the cells
def updater():


# create the board
spot_11 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=1, column=0)
spot_12 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=1, column=1)
spot_13 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=1, column=2)
spot_21 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=2, column=0)
spot_22 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=2, column=1)
spot_23 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=2, column=2)
spot_31 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=3, column=0)
spot_32 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=3, column=1)
spot_33 = Label(root, text="", borderwidth=1, relief="solid", width=10, height=5, font=("Arial", 20)).grid(row=3, column=2)



mainloop()