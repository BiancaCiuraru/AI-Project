from tkinter import *
from tkinter import ttk
from functools import partial
import make_rec as recommendations
import get_description as info


def draw():
    master = Tk()
    master.title('Movie Recommendations')
    master.geometry("604x253")
    master.resizable(False, False)

    style = ttk.Style(master)
    style.theme_use('clam')
    ttk.Style().configure("Treeview", fieldbackground="#e7eaef")
    ttk.Style().configure("Treeview.Heading", background="#05828e", borderwidth=0)

    style.configure('TButton', background='#05828e', foreground='black', font=('Times', '9', 'bold'), borderwidth=0)
    style.map("TButton", foreground=[("focus", "black"), ('pressed', 'black'), ('active', 'black')], background=[('pressed', '!disabled', '#05828e'), ('active', '#05828e')])
    
    drop = ttk.Combobox(master, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    drop.set("Nr Results")
    drop.grid(column=0, row=0)

    searchBar = ttk.Entry(master, width=56)
    searchBar.insert(0, "Enter Description")
    searchBar.bind("<FocusIn>", lambda _: searchBar.delete(0, 'end'))
    searchBar.grid(row=0, column=1)

    cols = ('Title', 'Genre', 'Description')
    listBox = ttk.Treeview(master, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=3)

    searchButton = ttk.Button(master, text="Search", command=partial(user_input, searchBar, listBox, drop), width=16)
    searchButton.grid(row=0, column=2)
    mainloop()


def user_input(searchBar, listBox, drop):
    listBox.delete(*listBox.get_children())

    nr_results = 10
    if drop.get() != "Nr Results":
        nr_results = drop.get()
    searchBarText = searchBar.get()

    i = 0
    for movie in recommendations.make_recommendations(searchBarText, int(nr_results)):
        title = movie[0][1]
        genres = info.get_description_genre(title)[0]
        description = info.get_description_genre(title)[1]
        if description == 'none':
            description = 'Description not found! Sorry!'
        if i % 2 == 0:
            listBox.insert("", "end", values=(title, genres, description))
        else:
            listBox.insert("", "end", values=(title, genres, description))
        i = i + 1
   
    return searchBarText

  
draw()
