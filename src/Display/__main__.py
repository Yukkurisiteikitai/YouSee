import sys
from tkinter import *

root = Tk()
root.title(u"YouSee-mainMenu")
root.geometry("1280x780")


#Chat 閲覧画面
frame = Frame(root)

sc = Scrollbar(frame)
sc.pack(side=RIGHT, fill=Y)

msgs = Listbox(frame,width=80, height=20, yscrollcommand=sc.set)
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# Input Text Space 入力画面
textF = Entry(root,font=("Courier", 10 ),width=30)
textF.pack()

def send_text_bot():
    query = textF.get()
    answer_from_bot = "hello"
    msgs.insert(END,f"you :{query}")
    msgs.insert(END,f"bot :{answer_from_bot}")
    textF.delete(0,END)
    msgs.yview(END)

btn = Button(root, text="質問をどうぞ", font=("Courier",10),bg="white",command=send_text_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

root.mainloop()

# test
root.after(10,send_text_bot)