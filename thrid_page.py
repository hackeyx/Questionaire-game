import tkinter as tk
from tkinter import messagebox


from PIL import Image, ImageTk

window = tk.Tk()
ico = Image.open('uuu.png')
window.iconbitmap("C:/Users/User/PycharmProjects/Questionaire")
my_image = ImageTk.PhotoImage(Image.open("uuu.png"))
window.wm_iconphoto(False, my_image)

window.geometry("5000x5000")
window.title("Dissect level 3")
window.configure(bg="#1B1B1B")
window.resizable(True, True)


def correct():
    messagebox.showinfo("CORRECT!!", "CORRECT")


def incorrect():
    messagebox.showinfo("WRONG!!", "WRONG")


# Question one
Question = tk.Label(window, text="Question1 Guess the word: the country comPutER, an a gram.", font=("Nyala", 10))
# representative
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=90, pady=40)

ButtonOne = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda: result1())
ButtonOne.configure(fg="black", bg="#0080FF")
ButtonOne.place(x=800, y=95)

label_entry_one = tk.Entry(window, font=("Arial", 14))
label_entry_one.place(x=550, y=100)

# side stuffs
def perv_level():
    window.destroy()
    import second_page

ButtonCall = tk.Button(window, text="Previous Level", height=1, width=13, borderwidth=3, font=("Stylus", 12), command=lambda:perv_level())
ButtonCall.configure(fg="black", bg="#0080FF")
ButtonCall.place(x=1100, y=50)


# Question two
Question = tk.Label(window, text="Question2. AETOS DIOS is possessed"
                                 " his possession represent a group in Episkyros."
                                 " just ask jerry maguire. who am i?", font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=120, pady=40)

ButtonTwo = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda: result2())
ButtonTwo.configure(fg="black", bg="#0080FF")
ButtonTwo.place(x=750, y=200)

label_entry_two = tk.Entry(window, font=("Stylus", 12))
label_entry_two.place(x=550, y=200)

# Question three
Question = tk.Label(window, text="Question3. How many number PIEce are there? ",
                    font=("Nyala", 10))
# 31.4 trillion numbers are in pi
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=150, pady=40)

ButtonThree = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda:result3 ())
ButtonThree.configure(fg="black", bg="#0080FF")
ButtonThree.place(x=750, y=300)

label_entry_three = tk.Entry(window, font=("stylus", 12))
label_entry_three.place(x=550, y=300)
# Question four
Question = tk.Label(window, text="Question4. I am laced twice in eternity and always within sight. What could I be?",
                    font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=190, pady=40)

ButtonFour = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda: result4())
ButtonFour.configure(fg="black", bg="#0080FF")
ButtonFour.place(x=750, y=400)

label_entry_four = tk.Entry(window, font=("stylus", 12))
label_entry_four.place(x=550, y=400)

# Question five
Question = tk.Label(window, text="Question5 "
                                 "Guess the common phrase: I am having feelings "
                                 "as long as the sun shine", font=("Nyala", 10))
# i am feeling under the weather
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=230, pady=40)

ButtonFive = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda:result5 ())
ButtonFive.configure(fg="black", bg="#0080FF")
ButtonFive.place(x=750, y=500)

label_entry_five = tk.Entry(window, font=("stylus", 12))
label_entry_five.place(x=550, y=500)

# Question six
Question = tk.Label(window, text="Question6. what am i referring to?-"
                                 " if you have a thousand words, you dont need to shoot.", font=("Nyala", 10))
# picture
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=270, pady=40)

ButtonSix = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda:result6 ())
ButtonSix.configure(fg="black", bg="#0080FF")
ButtonSix.place(x=750, y=600)

label_entry_six = tk.Entry(window, font=("stylus", 12))
label_entry_six.place(x=550, y=600)
ButtonNP = tk.Button(window, text="DONE", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                     command=lambda: okay3())
ButtonNP.configure(fg="black", bg="#0080FF")
ButtonNP.place(x=1100, y=660)


def okay3():
    window.destroy()
    import optbut2

# result display
def result1():
    if label_entry_one.get().lower == "representative":
        return correct()
    elif label_entry_one.get().lower() == "rep":
        return correct()
    else:
        return incorrect()

def result2():
    if label_entry_two.get().lower() == "jeffrey lurie":
        return correct()
    else:
        return incorrect()
def result3():
    if label_entry_three.get().lower() == "31.4 trillion":
        return correct()
    elif label_entry_three.get() == "31,415,926,535,897":
        return correct()
    else:
        return incorrect()

def result4():
    if label_entry_four.get().lower() == "the letter t":
        return correct()
    elif label_entry_four.get().lower() == "t":
        return correct()
    else:
        return incorrect()

def result5():
    if label_entry_five.get().lower() == "i am feeling under the weather":
        return correct()
    elif label_entry_five.get().upper() == "FEELING UNDER THE WEATHER":
        return correct()
    else:
        return incorrect()

def result6():
    if label_entry_six.get().upper() == "PICTURE":
        return correct()
    elif label_entry_six.get().lower() == "a picture":
        return correct()
    elif label_entry_six.get().lower() == "pictures":
        return correct()
    else:
        return incorrect()
window.mainloop()
