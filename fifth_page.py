import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

window = tk.Tk()
ico = Image.open('uuu.png')
window.iconbitmap("C:/Users/User/PycharmProjects/Questionaire")
my_image = ImageTk.PhotoImage(Image.open("uuu.png"))
window.wm_iconphoto(False, my_image)

window.geometry("5000x5000")
window.title("Dissect level 5")
window.configure(bg="#000000")
window.resizable(True, True)


def correct():
    messagebox.showinfo("CORRECT!!", "CORRECT")


def incorrect():
    messagebox.showinfo("WRONG!!", "WRONG")


# Question one
Question = tk.Label(window, text="my Late Registration into College made me move to the west, like the guy YEsterday "
                                 "who Droupout before he's Graduation because of a Dark Fantasy is thought was Beautiful", font=("Nyala", 10))
Question.configure(fg="white", bg="#000000")
Question.pack(padx=90, pady=40)

ButtonOne = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda: result1())
ButtonOne.configure(fg="black", bg="#191970")
ButtonOne.place(x=800, y=95)

label_entry_one = tk.Entry(window, font="Arial 14")
label_entry_one.place(x=550, y=100)


# side stuffs
def perv_level():
    window.destroy()
    import fourth_page

ButtonCall = tk.Button(window, text="Previous level", height=1, width=13, borderwidth=3, font=("Stylus", 12), command=lambda:perv_level())
ButtonCall.configure(fg="black", bg="#191970")
ButtonCall.place(x=1100, y=5)


# Question two
Question = tk.Label(window, text="Question2: Talk and you break it but you have an action you take to "
                                 "keep it unbroken. they are just the same words but misspelled", font=("Nyala", 10))
Question.configure(fg="white", bg="#000000")
Question.pack(padx=100, pady=70)

ButtonTwo = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda: result2())
ButtonTwo.configure(fg="black", bg="#191970")
ButtonTwo.place(x=800, y=220)

label_entry_two = tk.Entry(window, font="Arial 14")
label_entry_two.place(x=550, y=220)



# Question three
Question = tk.Label(window, text="Question3. what is the subject of this - 'cow herds telling you to moo! or they "
                                 "call bull (he's) on you' ",
                    font=("Nyala", 10))
Question.configure(fg="white", bg="#000000")
Question.pack(padx=100, pady=0)

ButtonThree = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda:result3 ())
ButtonThree.configure(fg="black", bg="#191970")
ButtonThree.place(x=800, y=320)

label_entry_three = tk.Entry(window, font=("Arial", 14))
label_entry_three.place(x=550, y=325)

# Question four
Question = tk.Label(window, text="Question 4: Sanskrit avatra; Poseidon, Gaia, Hephaestus and ___________", font=("Nyala", 10))
Question.configure(fg="white", bg="#000000")
Question.pack(padx=110, pady=90)

ButtonFour = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda: result4())
ButtonFour.configure(fg="black", bg="#191970")
ButtonFour.place(x=800, y=425)

label_entry_four = tk.Entry(window, font="Arial 14")
label_entry_four.place(x=550, y=430)

# Question five
Question = tk.Label(window, text="Question 5: Give me two U's then we call it a _____", font=("Nyala", 10))
Question.configure(fg="white", bg="#000000")
Question.pack(padx=0, pady=0)

ButtonFive = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda:result5 ())
ButtonFive.configure(fg="black", bg="#191970")
ButtonFive.place(x=800, y=535)

label_entry_five = tk.Entry(window, font="Arial 14")
label_entry_five.place(x=550, y=540)


# Question six
Question = tk.Label(window, text="Question6. what is the foundation of this sentence? SAr, MADam? iS the "
                                 "foundAtion, also,hold Ma phone for the last quest on "
                                 "this App. so Do it.", font=("Nyala", 10))
Question.configure(fg="white", bg="#000000")
Question.pack(padx=100, pady=85)

ButtonSix = tk.Button(window, text="sumbit", height=1, width=10, borderwidth=3, font=("Stylus", 12),
                      command=lambda:result6 ())
ButtonSix.configure(fg="black", bg="#191970")
ButtonSix.place(x=800, y=625)

label_entry_six = tk.Entry(window, font="Arial 14")
label_entry_six.place(x=550, y=630)


ButtonNP = tk.Button(window, text="DONE", height=1, width=20, borderwidth=2, font=("Stylus", 12),
                     command=lambda: okay5())
ButtonNP.configure(fg="black", bg="#191970")
ButtonNP.place(x=1100, y=660)


def okay5():
    window.destroy()
    import introduction

# result display
def result1():
    if label_entry_one.get().lower == "kanye west":
        return correct()
    elif label_entry_one.get().lower() == "ye":
        return correct()
    else:
        return incorrect()

def result2():
    if label_entry_two.get().lower() == "silent and listen":
        return correct()
    if label_entry_two.get().lower() == "listen and silent":
        return correct()
    else:
        return incorrect()
def result3():
    if "bully" in label_entry_three.get() :
        return correct()
    elif "bullies" in label_entry_three.get() :
        return correct()
    elif "cowards" in label_entry_three.get() :
        return correct()
    else:
        return incorrect()

def result4():
    if label_entry_four.get().lower() == "vayu":
        return correct()
    else:
        return incorrect()

def result5():
    if label_entry_five.get().lower() == "win":
        return correct()
    elif label_entry_five.get().upper() == "A WIN":
        return correct()
    else:
        return incorrect()

def result6():
    if label_entry_six.get().upper() == "samad":
        return correct()
    elif label_entry_six.get().lower() == "samad samad":
        return correct()
    else:
        return incorrect()

window.mainloop()
