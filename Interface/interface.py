from tkinter import *
from tkinter import ttk

master = Tk()
master.geometry("300x100+10+20")
Label(master, text='Add a description').grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)


def user_input():
    query = e1.get()
    return query


def get_result():
    window = Tk()
    cols = ('Title', 'Genre', 'Description')
    Label(window, text="Results").grid(row=0)
    listBox = ttk.Treeview(window, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)


b1 = Button(master, text="Search", command=user_input)
b2 = Button(master, text="View results", command=get_result)

b1.grid(row=0, column=2)
b2.grid(row=1, column=1)
mainloop()
