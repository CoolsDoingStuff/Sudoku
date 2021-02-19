from tkinter import *

root = Tk()
root.title("Super Cool Super Slick Super Sudoku Solver")
#root.geometry("400x450")

# add a title to the Sudoku board
visible_title = Label(root, text="Sudoku? Ha! Watch this!", font=("Arial", 30))
visible_title.grid(row=0, column=0, columnspan=3)

add_num = Entry(root, width=10)
add_num.grid(row=4, column=1, columnspan=3)

# create a function that updates one of the cells. I want to click, put a number and hit enter, done.
def updater():

    return


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

but11 = Button(root, width=21, height=10, relief="flat", command=lambda: updater()).grid(row=1, column=0)
but12 = Button(root, width=21, height=10, relief="flat", command=lambda: updater()).grid(row=1, column=1)
but13 = Button(root, width=21, height=10, relief="flat", command=lambda: updater()).grid(row=1, column=2)
but21 = Button(root, width=21, height=10, relief="flat", command=lambda: updater()).grid(row=2, column=0)
but22 = Button(root, width=21, height=10, relief="flat", command=lambda: updater()).grid(row=2, column=1)
but23 = Button(root, width=21, height=10, relief="flat", command=lambda: updater()).grid(row=2, column=2)
but31 = Button(root, width=21, height=10, relief="flat", command=lambda: updater()).grid(row=3, column=0)
but32 = Button(root, width=21, height=10, relief="flat", command=lambda: updater()).grid(row=3, column=1)
but33 = Button(root, width=21, height=10, relief="flat", command=lambda: updater()).grid(row=3, column=2)

# Need to build a function that updates the button text. See link here:
# https://stackoverflow.com/questions/32615440/python-3-tkinter-how-to-update-button-text/53201471


mainloop()