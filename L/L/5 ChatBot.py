from tkinter import *  # Import everything from the tkinter library

root = Tk()  # Create a Tkinter window
root.title("Chatbot")  # Set the title of the window to "Chatbot"

def send():  # Define a function named "send"
    send = "You -> " + e.get()  # Create a message string indicating user input
    txt.insert(END, "\n" + send)  # Insert the message string into the Text widget
    user = e.get().lower()  # Get the user input from the entry field and convert it to lowercase
    if user == "hello":  # Check if the user input is "hello"
        txt.insert(END, "\n" + "Bot -> Hi")  # Insert a response from the bot into the Text widget
    elif user in ["hi", "hii", "hiii"]:  # Check if the user input is any variation of "hi"
        txt.insert(END, "\n" + "Bot -> Hello")  # Insert a response from the bot into the Text widget
    elif user == "how are you":  # Check if the user input is "how are you"
        txt.insert(END, "\n" + "Bot -> Fine! and you?")  # Insert a response from the bot into the Text widget
    elif user in ["fine", "i am good", "i am doing good"]:  # Check if the user input indicates they are feeling fine
        txt.insert(END, "\n" + "Bot -> Great! How can I help you?")  # Insert a response from the bot into the Text widget
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't get you")  # Insert a generic response from the bot into the Text widget
        e.delete(0, END)  # Clear the entry field

txt = Text(root)  # Create a Text widget within the Tkinter window
txt.grid(row=0, column=0, columnspan=2)  # Place the Text widget in the window
e = Entry(root, width=100)  # Create an Entry widget within the Tkinter window for user input
e.grid(row=1, column=0)  # Place the Entry widget in the window
send = Button(root, text="Send", command=send)  # Create a Button widget for sending messages
send.grid(row=1, column=1)  # Place the Button widget in the window
root.mainloop()  # Start the main event loop to display the window and handle user interactions
