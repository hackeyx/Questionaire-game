import tkinter as tk
from tkinter import messagebox


window2 = tk.Tk()

window2.geometry("5000x5000")
window2.title("Dissect level 2")
window2.configure(bg="#1B1B1B")
window2.resizable(True, True)


def correct():
    messagebox.showinfo("CORRECT!!", "CORRECT")


def incorrect():
    messagebox.showinfo("WRONG!!", "WRONG")


# Question one
Question = tk.Label(window2, text="Quetsion1. He explained not to get yourself lost and a fan killed himself, his wife "
                                 "and his unborn daughter in a car that went straight into a ocean from a bridge. who is he?",
                    font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=90, pady=40)

ButtonOne = tk.Button(window2, text="Submit", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                      command=lambda: result1())
ButtonOne.configure(fg="black", bg="#30D5C8")
ButtonOne.place(x=800, y=95)

label_entry_one = tk.Entry(window2, font=("Arial", 14))
label_entry_one.place(x=550, y=100)

# side stuffs
def perv_level():
    window2.destroy()
    import main

ButtonCall = tk.Button(window2, text="Previous Level", height=1, width=13, borderwidth=3, font=("Stylus", 12), command=lambda:perv_level())
ButtonCall.configure(fg="black", bg="#30D5C8")
ButtonCall.place(x=1100, y=5)

# Question two
Question = tk.Label(window2, text="Question2. what is the theme of the sentence?: A men is 2/7 Germany,1/6"
                                 " zambia and 2/7 Eritrea, so an a gram is dog", font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=120, pady=40)

ButtonTwo = tk.Button(window2, text="Sumbit", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                      command=lambda: result2())
ButtonTwo.configure(fg="black", bg="#30D5C8")
ButtonTwo.place(x=800, y=200)

label_entry_two = tk.Entry(window2, font=("Stylus", 12))
label_entry_two.place(x=550, y=200)

# Question three
Question = tk.Label(window2, text="Question3. Be polite, apPLE A Day by using the word.",
                    font=("Nyala", 10))
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=150, pady=40)

ButtonThree = tk.Button(window2, text="Submit", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                        command=lambda: result3())
ButtonThree.configure(fg="black", bg="#30D5C8")
ButtonThree.place(x=800, y=305)

label_entry_three = tk.Entry(window2, font=("stylus", 12))
label_entry_three.place(x=550, y=300)
# Question four
Question = tk.Label(window2, text="Question4? It is popular like my favorite category, cause it is both",
                    font=("Nyala", 10))
# pop is popular that's why it's called pop and it's my favorite category/genre (not actually)
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=190, pady=40)

ButtonFour = tk.Button(window2, text="Submit", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                       command=lambda: result4())
ButtonFour.configure(fg="black", bg="#30D5C8")
ButtonFour.place(x=800, y=410)

label_entry_four = tk.Entry(window2, font=("stylus", 12))
label_entry_four.place(x=550, y=410)

# Question five
Question = tk.Label(window2, text="Question5. What has ten letters and starts with gas?",
                    font=("Nyala", 10))  # automobile
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=230, pady=40)

ButtonFive = tk.Button(window2, text="Submit", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                       command=lambda: result5())
ButtonFive.configure(fg="black", bg="#30D5C8")
ButtonFive.place(x=800, y=510)

label_entry_five = tk.Entry(window2, font=("stylus", 12))
label_entry_five.place(x=550, y=510)

# Question six
Question = tk.Label(window2, text="Question6. You are my brother, but I am not your brother. Who am I?",
                    font=("Nyala", 10))
# sister
Question.configure(fg="white", bg="#1B1B1B")
Question.pack(padx=270, pady=40)

ButtonSix = tk.Button(window2, text="Sumbit", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                      command=lambda: result6())
ButtonSix.configure(fg="black", bg="#30D5C8")
ButtonSix.place(x=800, y=600)

label_entry_six = tk.Entry(window2, font=("stylus", 12))
label_entry_six.place(x=550, y=600)
ButtonNP = tk.Button(window2, text="DONE", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                     command=lambda: okay2())
ButtonNP.configure(fg="black", bg="#30D5C8")
ButtonNP.place(x=1100, y=660)


def okay2():
    window2.destroy()
    import introduction


# result display
def result1():
    if label_entry_one.get().lower() == "eminem":
        return correct()
    elif label_entry_one.get().lower() == "slim shady":
        return correct()
    elif label_entry_one.get().lower() == "marshall mathers":
        return correct()
    else:
        return incorrect()


def result2():
    if label_entry_two.get().lower() == "christian religion":
        return correct()
    else:
        return incorrect()


def result3():
    if label_entry_three.get().lower() == "please":
        return correct()
    else:
        return incorrect()


def result4():
    if label_entry_four.get().lower() == "pop genre":
        return correct()
    elif label_entry_four.get() == "pop":
        return correct()
    else:
        return incorrect()


def result5():
    if label_entry_five.get().lower() == "automobile":
        return correct()
    else:
        return incorrect()


def result6():
    if label_entry_six.get().lower() == "your sister":
        return correct()
    elif label_entry_six.get().lower() == "sister":
        return correct()
    else:
        return incorrect()


window2.mainloop()
