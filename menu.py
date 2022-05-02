from bookcheckout import book_checkout
from bookreturn import book_return
from booksearch import book_search

# I first import the functions, book_search, book_checkout and book_search that
# I have made so that they are able to be used in this file.


def lib_menu():
    # This function serves to be used as a menu interface as an alternative to
    # tkinter.

    print("\n")
    print("++++++++++++++++++++++++++++++++++++++")
    print("+--------------Library---------------+")
    print("+-------------Management-------------+")
    print("+---------------System---------------+")
    print("++++++++++++++++++++++++++++++++++++++")
    print("Please select a function below")
    print("{[bs] Search for a book in the system}")
    print("{[bc] Check a book out of the system}")
    print("{[br] Return a book to the system}")
    print("{[ex] Exit the program}")


while True:
    # A while loop is used with an unchanging boolean (as it is not assigned to
    # a variable) to continue iterating the menu in th console.

    lib_menu()
    lib_function = input("\t\n:~")
    # The interface function is called and an input is requested in order to
    # access the system's functions.

    if lib_function == "bs":
        # The book searching function.

        book_title = input("What book would you like to search for?\n")
        book_search(book_title)
    elif lib_function == "bc":
        # The book checkout function.

        book_id = input("Please enter the ID of the book you wish to check "
                        "out:\n")
        member_id = input("Please enter the ID of the member who is checking "
                          "out the book:\n")
        member_id_int = int(member_id)
        book_checkout(book_id, member_id, member_id_int)

    elif lib_function == "br":
        # The book return function.

        book_id = input("Enter the ID of the book you would like to return:\n")
        book_return(book_id)
        
    elif lib_function == "ex":
        # And finally an exit command to end the program.

        quit()
