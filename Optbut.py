import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
ico = Image.open('uuu.png')
window.iconbitmap("C:/Users/User/PycharmProjects/Questionaire")
my_image = ImageTk.PhotoImage(Image.open("uuu.png"))
window.wm_iconphoto(False, my_image)
tabkepper = ttk.Notebook(window)

window.geometry("1000x1000")
window.title("Dissect")
window.resizable(True, True)

tab1 = Frame(tabkepper, width=1000, height=1000, bg='black')
tab2 = Frame(tabkepper, width=1000, height=1000, bg='black')
tab1.configure(bg="#000000")
label = tk.Label(tab1, text="Levels Of This Game", font=("Raleway", 20))
label.configure(fg="white", bg="black")
label.pack(padx=100, pady=30)

but1 = tk.Button(tab1, text="Level 1", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                 command=lambda: one())
but1.configure(fg="white", bg="#000000")
but1.place(x=650, y=100)

but2 = tk.Button(tab1, text="Level 2", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                  command=lambda: two())
but2.configure(fg="white", bg="#000000")
but2.place(x=650, y=220)

but3 = tk.Button(tab1, text="Level 3", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                  command=lambda: three())
but3.configure(fg="white", bg="#000000")
but3.place(x=650, y=340)

but4 = tk.Button(tab1, text="Level 4", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                  command=lambda: four())
but4.configure(fg="white", bg="#000000")
but4.place(x=650, y=460)

but5 = tk.Button(tab1, text="Level 5", width=5, height=2, borderwidth=15, font=("Helvetica", 13),
                  command=lambda: five())
but5.configure(fg="white", bg="#000000")
but5.place(x=650, y=575)

tabkepper.pack(fill="both", expand=1)
tabkepper.pack(fill="both", expand=1)

tabkepper.add(tab1, text="Play Game")
tabkepper.add(tab2, text="About")

Question = tk.Label(tab2, text="""
    An Amazing riddle and complex puzzle game, which requires alot of thinking and mental energy but fun at the same time,
    you May feel free to check the internet for clues that can help ;)  
    it comprises of 5 levels which gets more difficulty every level you go and the next level is not going to be accessible 
    if the previous one as not been completed before.        

    About The creator: The name is salami samad and i created this for you to be able to test you thinking and mind puzzling 
    abilities, i'm a polymath, free thinker and a lover of knowledge. you can find me on twitter (@Salamisamad5). Enough 
    about me, you play the game, if you dare. 
    ENJOY :)

    """, font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=90, pady=50)


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


