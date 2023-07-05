import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

window = tk.Tk()
ico = Image.open('uuu.png')
window.iconbitmap("C:/Users/User/PycharmProjects/Questionaire")
my_image = ImageTk.PhotoImage(Image.open("uuu.png"))
window.wm_iconphoto(False, my_image)

window.geometry("5000x5000")
window.title("Dissect level 4")
window.configure(bg="#0E0E10")
window.resizable(True, True)


def correct():
    messagebox.showinfo("CORRECT!!", "CORRECT")


def incorrect():
    messagebox.showinfo("WRONG!!", "WRONG")


# Question one
Question = tk.Label(window, text="Question1: what am i referring to?- Madonna was so beautiful, we HEARD and observed"
                                 " her for so long. it was lisa", font=("Nyala", 10))
Question.configure(fg="white", bg="#0E0E10")
Question.pack(padx=90, pady=40)

ButtonOne = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda: result1())
ButtonOne.configure(fg="black", bg="#0047ab")
ButtonOne.place(x=800, y=75)

label_entry_one = tk.Entry(window, font=("Arial", 14))
label_entry_one.place(x=550, y=80)

# side stuffs
def perv_level():
    window.destroy()
    import thrid_page

ButtonCall = tk.Button(window, text="Previous Level", height=1, width=13, borderwidth=3, font=("Stylus", 12), command=lambda:perv_level())
ButtonCall.configure(fg="black", bg="#0047ab")
ButtonCall.place(x=1100, y=50)


# Question two
QuestionS = tk.Label(window, text="Like getting A LOAN when starting a business,\n"
                                  " So Becoming a lone wolf When You Need To Think.\n"
                                  "which means _______is not bad                         ", font=("Nyala", 10))
QuestionS.configure(fg="white", bg="#0E0E10")
QuestionS.pack(padx=130, pady=40)

ButtonTwo = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda: result2())
ButtonTwo.configure(fg="black", bg="#0047ab")
ButtonTwo.place(x=750, y=205)

label_entry_two = tk.Entry(window, font=("Stylus", 12))
label_entry_two.place(x=550, y=210)

# Question three
Question = tk.Label(window, text="Question3. The more you take, the more you leave behind. What am I?",
                    font=("Nyala", 10))
Question.configure(fg="white", bg="#0E0E10")
Question.pack(padx=170, pady=40)

ButtonThree = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                        command=lambda: result3())
ButtonThree.configure(fg="black", bg="#0047ab")
ButtonThree.place(x=750, y=305)

label_entry_three = tk.Entry(window, font=("stylus", 12))
label_entry_three.place(x=550, y=310)
# Question four
Question = tk.Label(window, text="How many words are in a Dictionary? ", font=("Nyala", 10))
Question.configure(fg="white", bg="#0E0E10")
Question.pack(padx=210, pady=40)

ButtonFour = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                       command=lambda: result4())
ButtonFour.configure(fg="black", bg="#0047ab")
ButtonFour.place(x=750, y=415)

label_entry_four = tk.Entry(window, font=("stylus", 12))
label_entry_four.place(x=550, y=420)

# Question five
Question = tk.Label(window, text="What i'm i referring to?- betray Pride as you turn Scar.\n"
                                 "For you add a King and a Gift and gives you a member of the Pride ", font=("Nyala", 10))
Question.configure(fg="white", bg="#0E0E10")
Question.pack(padx=350, pady=40)

ButtonFive = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                       command=lambda: result5())
ButtonFive.configure(fg="black", bg="#0047ab")
ButtonFive.place(x=750, y=525)

label_entry_five = tk.Entry(window, font=("stylus", 12))
label_entry_five.place(x=550, y=530)

# Question six
Question = tk.Label(window, text="You count my silly ables that helps me to form this sentence.", font=("Nyala", 10))
Question.configure(fg="white", bg="#0E0E10")
Question.pack(padx=410, pady=40)

ButtonSix = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda: result6())
ButtonSix.configure(fg="black", bg="#0047ab")
ButtonSix.place(x=750, y=620)

label_entry_six = tk.Entry(window, font=("stylus", 12))
label_entry_six.place(x=550, y=625)

ButtonNP = tk.Button(window, text="DONE", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                     command=lambda: okay4())
ButtonNP.configure(fg="black", bg="#0047ab")
ButtonNP.place(x=1100, y=660)


def okay4():
    window.destroy()
    from optbut3 import whole


# result display
def result1():
    if label_entry_one.get().lower == "mona lisa":
        return correct()
    else:
        return incorrect()


def result2():
    if label_entry_two.get().lower() == "alone":
        return correct()
    elif label_entry_two.get().lower() == "being alone":
        return correct()
    elif label_entry_two.get().lower() == "solitude":
        return correct()
    else:
        return incorrect()


def result3():
    if label_entry_three.get().lower() == "footsteps":
        return correct()
    elif label_entry_three.get().lower() == "my footsteps":
        return correct()
    else:
        return incorrect()


def result4():
    if label_entry_four.get().lower() == "Two. A & Dictionary":
        return correct()
    elif label_entry_four.get().lower() == "two":
        return correct()
    elif label_entry_four.get().lower() == "two words":
        return correct()
    elif label_entry_four.get().lower() == "two word":
        return correct()
    elif label_entry_four.get() == "2":
        return correct()
    else:
        return incorrect()


def result5():
    if label_entry_five.get().lower() == "the lion king":
        return correct()
    elif label_entry_five.get().lower() == "lion king":
        return correct()
    else:
        return incorrect()


def result6():
    if label_entry_six.get() == "15":
        return correct()
    elif label_entry_six.get().lower() == "15 syllables":
        return correct()
    elif label_entry_six.get().lower() == "fifteen syllables":
        return correct()
    else:
        return incorrect()


window.mainloop()
