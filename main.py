import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

window = tk.Tk()
ico = Image.open('uuu.png')
window.iconbitmap("C:/Users/User/PycharmProjects/Questionaire")
my_image = ImageTk.PhotoImage(Image.open("uuu.png"))
window.wm_iconphoto(False, my_image)

window.geometry("5000x5000")
window.title("Dissect Level 1")
window.configure(bg="#1B1B1B")
window.resizable(True, True)


def correct():
    messagebox.showinfo("CORRECT!!", "CORRECT")


def incorrect():
    messagebox.showinfo("WRONG!!", "WRONG")


# Question one
Question = tk.Label(window, text="Question1: I created a tic-tac-toe game was i was 13, can possibly read 150 pages in"
                                 " an hour. I've not only got fame to my name but i have money to it"
                                 " (quiet literally).who am i?"
                    , font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=90, pady=40)

ButtonOne1 = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                       command=lambda: result1())
ButtonOne1.configure(fg="black", bg="#ADD8E6")
ButtonOne1.place(x=800, y=95)

label_entry_one = tk.Entry(window, font=("Arial", 14))
label_entry_one.place(x=550, y=100)


# side stuffs
def perv_level():
    window.destroy()
    import introduction


ButtonCall = tk.Button(window, text="Back to intro", height=1, width=15, borderwidth=3, font=("Stylus", 12),
                       command=lambda: perv_level())
ButtonCall.configure(fg="black", bg="#ADD8E6")
ButtonCall.place(x=1100, y=5)

# Question two
Question = tk.Label(window, text="Question2. What is 3/7 chicken, 2/3 cat, and 2/4 goat?", font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=120, pady=40)

ButtonTwo1 = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                       command=lambda: [result2()])
ButtonTwo1.configure(fg="black", bg="#ADD8E6")
ButtonTwo1.place(x=750, y=200)

label_entry_two = tk.Entry(window, font=("Stylus", 12))
label_entry_two.place(x=550, y=200)

# Question three
Question = tk.Label(window, text="Question3. Try to link in this occurrence to a president: he married in he's 30s to"
                                 " a women who were in their 20s, he was shot in the head and he was shot on a friday",
                    font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=150, pady=40)

ButtonThree1 = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                         command=lambda: result3())
ButtonThree1.configure(fg="black", bg="#ADD8E6")
ButtonThree1.place(x=750, y=300)

label_entry_three = tk.Entry(window, font=("stylus", 12))
label_entry_three.place(x=550, y=310)
# Question four
Question = tk.Label(window, text="Question4. when i'm angry, i get flipped and turned to a punctuation. which"
                                 " of it am i?", font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=190, pady=40)

ButtonFour1 = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                        command=lambda: result4())
ButtonFour1.configure(fg="black", bg="#ADD8E6")
ButtonFour1.place(x=750, y=400)

label_entry_four = tk.Entry(window, font=("stylus", 12))
label_entry_four.place(x=550, y=410)

# Question five
Question = tk.Label(window, text="Question5. If you throw a blue stone into the Red Sea, what will it become?",
                    font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=230, pady=40)

ButtonFive1 = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                        command=lambda: result5())
ButtonFive1.configure(fg="black", bg="#ADD8E6")
ButtonFive1.place(x=750, y=500)

label_entry_five = tk.Entry(window, font=("stylus", 12))
label_entry_five.place(x=550, y=510)

# Question six
Question = tk.Label(window, text="Question6. hey PAL, who's name backward IN a family is a DROME?",
                    font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=270, pady=40)

ButtonSix1 = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                       command=lambda: result6())
ButtonSix1.configure(fg="black", bg="#ADD8E6")
ButtonSix1.place(x=750, y=600)

label_entry_six = tk.Entry(window, font=("stylus", 12))
label_entry_six.place(x=550, y=610)

ButtonNP = tk.Button(window, text="DONE", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                     command=lambda: okay1())
ButtonNP.configure(fg="black", bg="#ADD8E6")
ButtonNP.place(x=1100, y=660)


def okay1():
    window.destroy()
    import Optbut


# result display
def result1():
    if label_entry_one.get().lower() == "bill gates":
        return correct()
    elif label_entry_one.get().lower() == "bill gate":
        return correct()
    else:
        return incorrect()


def result2():
    if label_entry_two.get().lower() == "chicago":
        return correct()
    else:
        return incorrect()


def result3():
    if label_entry_three.get().lower() == "abraham lincoln":
        return correct()
    else:
        return incorrect()


def result4():
    if label_entry_four.get().lower() == "exclamation mark":
        return correct()
    elif label_entry_four.get().lower() == "exclamation":
        return correct()
    else:
        return incorrect()


def result5():
    if label_entry_five.get().lower() == "it becomes wet ":
        return correct()
    elif label_entry_five.get().lower() == "wet":
        return correct()
    else:
        return incorrect()


def result6():
    if label_entry_six.get().lower() == "bro":
        return correct()
    else:
        return incorrect()


window.mainloop()
