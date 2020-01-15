from tkinter import *
from tkinter import ttk
from functools import partial


def draw():
    master = Tk()
    master.geometry("605x255")
    master.resizable(False,False)

    drop = ttk.Combobox(master,values=["1","2","3","4","5","6","7","8","9","10"])
    drop.set("Nr Results")
    drop.grid(column=0,row=0)



    searchBar = Entry(master,width = 55)
    searchBar.grid(row=0, column=1)

    cols = ('Title', 'Genre', 'Description')
    listBox = ttk.Treeview(master, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1,column=0,columnspan=3)
    
    searchButton = Button(master, text="Search", command= partial(user_input,searchBar,listBox,drop),relief=GROOVE,width=16)
    searchButton.grid(row=0, column=2)

    
    mainloop()

def user_input(searchBar,listBox,drop):
    nr_results = 10
    if(drop.get()!="Nr Results"):
        nr_results = drop.get()
    print(nr_results)
    searchBarText = searchBar.get()
    listBox.insert("","end", values=("a","b","c")) #aici pui din ce returneaza AI ul , a-primul camp, b-al doilea etc.
    return searchBarText

draw()