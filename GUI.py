from booksearch import book_search
from bookcheckout import book_checkout
from bookreturn import book_return
import tkinter as tk
from tkinter import *

print(__name__)

def search_window():
    search_window = Tk()
    search_window.title("Book Search")
    search_window.geometry("300x400")

    searchframe = LabelFrame(search_window)

    searchEntry = Entry(searchframe, width=15)

    doSearch = Button(searchframe, text="Lookup Book ID", command=book_search)

    lblResult = Label(searchframe, text="Results  ")

    search_back = tk.Button(searchframe, text="Back to Menu", width=25, command=search_window.destroy)

    searchframe.pack(fill="both", expand="yes")
    searchEntry.pack(side=tk.TOP)
    doSearch.pack(side=tk.TOP)
    lblResult.pack(side=tk.TOP)
    search_back.pack(side=tk.BOTTOM)

    search_window.mainloop()


def checkout_window():
    checkout_window = Tk()
    checkout_window.title("Book Search")
    checkout_window.geometry("300x400")

    checkoutframe = LabelFrame(checkout_window)
    checkoutframe.pack(fill="both", expand="yes")

    checkout_back = tk.Button(checkoutframe, text="Back to Menu", width=25, command=checkout_window.destroy)
    checkout_back.pack(side=tk.BOTTOM)

    checkout_window.mainloop()


def return_window():
    return_window = Tk()
    return_window.title("Book Return")
    return_window.geometry("300x400")

    returnframe = LabelFrame(return_window)
    returnframe.pack(fill="both", expand="yes")

    search_back = tk.Button(returnframe, text="Back to Menu", width=25, command=return_window.destroy)
    search_back.pack(side=tk.BOTTOM)

    return_window.mainloop()



root = Tk()
root.title("Simple Library Management System")
root.geometry("300x400")

labelframe = LabelFrame(root, text="Simple Library Management System")
labelframe.pack(fill="both", expand="yes")

book_search = tk.Button(labelframe, text="Search for a book", width=25, command=search_window)
book_checkout = tk.Button(labelframe, text="Check out a book", width=25, command=checkout_window)
book_return = tk.Button(labelframe, text="Return a book", width=25, command=return_window)
book_weed = tk.Button(labelframe, text="Use the weeding feature", width=25)
exit_button = tk.Button(labelframe, text="Exit", width=25, command=quit)

book_search.pack(side=tk.TOP)
book_checkout.pack(side=tk.TOP)
book_return.pack(side=tk.TOP)
book_weed.pack(side=tk.TOP)
exit_button.pack(side=tk.BOTTOM)













root.mainloop()