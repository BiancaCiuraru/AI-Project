from tkinter import *
from tkinter import ttk
from functools import partial


def draw():
    master = Tk()
    master.geometry("605x255")
    master.resizable(False,False)

    searchBar = Entry(master,width = 80)
    searchBar.grid(row=0, column=0, columnspan = 2)

    cols = ('Title', 'Genre', 'Description')
    listBox = ttk.Treeview(master, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1,column=0,columnspan=3)
    
    searchButton = Button(master, text="Search", command= partial(user_input,searchBar,listBox),relief=GROOVE,width=16)
    searchButton.grid(row=0, column=2)

    
    mainloop()

def user_input(searchBar,listBox):
    searchBarText = searchBar.get()
    listBox.insert("","end", values=("a","b","c")) #aici pui din ce returneaza AI ul , a-primul camp, b-al doilea etc.
    return searchBarText

draw()