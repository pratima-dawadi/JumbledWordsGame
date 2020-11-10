from tkinter import *
import random
from tkinter import messagebox

words = ["hargcer", "tertaby", "dicnemie", "tansd", "hopne", "yothpn", "taplop", "tonuamiato"]
answers = ["charger", "battery", "medicine", "stand", "phone", "python", "laptop", "automation"]
Score = {"score":0}

num = random.randrange(0, 8, 1)

def reset():
    global words, answers, num
    num = random.randrange(0, 8, 1)
    lbl.config(text=words[num])


def default():
    global words
    global answers
    global num
    lbl.config(text=words[num])
    e1.delete(0, END)

def checkans():
    global words, answers, num,score
    score = Score.get("score", 0)
    print(score)
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        e1.delete(0, END)
        reset()
        score=score+1
        Score["score"] = score
        myscore.config(text="Score  "+ str(score))



    else:
        messagebox.showinfo("Error", "This is a not correct answer")
        e1.delete(0, END)

root = Tk()
root.title("Jumbbled Game")
root.configure(background="black")
root.geometry("340x300")
root.resizable(0,0)

lbl = Label(root, text=("Jumbbled word here"), bg="black", fg="white", font=("Comic sans ms", 22))

lbl.pack(pady=8)
e1 = Entry(root)
e1.pack(pady=8, ipady=4, ipadx=8)
btn1 = Button(root, text="Check", font=("Verdana", 8), command=checkans, bg="grey", fg="yellow", relief=GROOVE,
              width=13, height=2)
btn1.pack(pady=8)
btn2 = Button(root, text="Reset", command=reset, bg="dark grey", fg="green", width=13, height=2)
btn2.pack(pady=8)
myscore=Label(root,text="Score  0",width=8,font=("Comic sans ms", 12))
myscore.pack(ipady=4,pady=2)

default()

root.mainloop()
