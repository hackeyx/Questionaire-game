import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
ico = Image.open('uuu.png')
window.iconbitmap("C:/Users/User/PycharmProjects/Questionaire")
my_image = ImageTk.PhotoImage(Image.open("uuu.png"))
window.wm_iconphoto(False, my_image)
window.configure()
window.geometry("1000x1000")
window.title("Dissect")
window.resizable(True, True)
window.configure(bg="#000000")


label = tk.Label(window, text="Levels Of This Game", font=("Raleway", 20))
label.configure(fg="white", bg="black")
label.pack(padx=100, pady=30)

but1 = tk.Button(window, text="Level 1", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                 command=lambda: one())
but1.configure(fg="white", bg="#000000")
but1.place(x=650, y=100)

but2 = tk.Button(window, text="Level 2", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                 command=lambda: two())
but2.configure(fg="white", bg="#000000")
but2.place(x=650, y=220)

but3 = tk.Button(window, text="Level 3", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                 command=lambda: three())
but3.configure(fg="white", bg="#000000")
but3.place(x=650, y=340)

but4 = tk.Button(window, text="Level 4", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                 command=lambda: four())
but4.configure(fg="white", bg="#000000")
but4.place(x=650, y=460)

but5 = tk.Button(window, text="Level 5", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                 command=lambda: five())
but5.configure(fg="white", bg="#000000")
but5.place(x=650, y=575)



def one():
    window.destroy()
    import main


def two():
    window.destroy()
    import second_page


def three():
    window.destroy()
    import thrid_page


def four():
    window.destroy()
    import fourth_page


def five():
    window.destroy()
    import fifth_page


window.mainloop()
