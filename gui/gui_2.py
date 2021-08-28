from tkinter import *
from tkinter import scrolledtext


def display():
    e.delete(0, END)  # Clear text before inserting new text
    e.insert(END, "Button Clicked")


def display_text():
    for i in range(25):
        T.insert(END, f'{i}\n')


root = Tk()

# Specify the size of the default window
root.geometry('400x350')

root.title("Weather Forecast")

label1 = Label(root, text="First GUI")
label1.grid(row=0, column=0)

button1 = Button(root, text='ClickMe', padx=20, command=display_text)
button1.grid(row=1, column=0)

# Disabled button
button2 = Button(root, text='ClickMe Too', state=DISABLED)
button2.grid(row=2, column=0)

# Exit button
button3 = Button(root, text='Exit', padx=20, command=root.destroy)
button3.grid(row=4, column=0)

# Input Box
e = Entry(root)
e.grid(row=1, column=1)

# Text Box
# T = Text(root, height=2, width=30)
# T.grid(row=3, column=1)

# Scrolling Text Box
T = scrolledtext.ScrolledText(root,width=30,height=10)
T.grid(row=3, column=1)

root.mainloop()
