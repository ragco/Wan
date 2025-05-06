from tkinter import *

root = Tk()
root.title("Chatbot")

def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)  # Insert newline character before sending the message
    user = e.get().lower()
    if user == "hello":
        txt.insert(END, "\n" + "Bot -> Hi")
    elif user in ["hi", "hii", "hiii"]:
        txt.insert(END, "\n" + "Bot -> Hello")
    elif user == "how are you":
        txt.insert(END, "\n" + "Bot -> Fine! and you?")
    elif user in ["fine", "i am good", "i am doing good"]:
        txt.insert(END, "\n" + "Bot -> Great! How can I help you?")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't get you")
        e.delete(0, END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send)
send.grid(row=1, column=1)  # Grid the button
root.mainloop()
