import csv
import datetime
import fileinput

# Imported CSV to make use of CSV functionality within the .txt based database.
# Imported datetime to make use dates and times with the intention to be used
# in the weeding module. Imported fileinput in order to make changes to the
# database in real time without having to manually handle files.

CURRENT_DATE_TIME = datetime.datetime.now()

# Again, this global constant is made for the logfile.txt and weeding module as
# a way to keep track of when books are being checked out and returned.

CURRENT_BOOK_IDs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Again I also made a list which serves as a constant which contains all of the
# unique book IDs that exist in the database to eliminate the need for data
# handling within the function.


def book_return(book_id):
    # This function serves as the method to return books to the database once
    # they have been returned to the library ready to be checked out again.

    if __name__ == "bookreturn":
        # This selection is to prevent the code from being run when imported
        # but only to run when called upon as seen in the testing section of
        # this module or the menu module.

        with fileinput.input(files='database.txt', inplace=True, mode='r') as f:
            # Similarly to the book check out function the fileinput module is
            # used to replace lines in the database.txt without having to
            # handle multiple versions of this file in real time.

            reader = csv.DictReader(f)

            print(",".join(reader.fieldnames))
            # Again the code is to use "," as the limiter and using the DictReader
            # print the field names or headers back into the database file.
            for row in reader:
                # This for loop iterates for every row that appears in
                # csv_reader.

                if book_id == row["book_id"] and row['member_id'] != 0:
                    # This selection statement check to see if the line it is
                    # currently iterating matches the user input for the
                    # "book_id".

                    row['member_id'] = "0"

                    # then the currently held value for "member_id" in the
                    # database is set to the user's input.

                print(",".join([row["book_id"], row["isbn"], row["title"],
                        row["author"], row["purchase_date"],row["member_id"]]))
            # It then prints the values it has read back into the file with the
            # updated information (if any).

            # The following code was to be used as functionality which supports
            # the logfile.txt and the weeding.py module.

            g = open("logfile.txt", "a")
            # Here the file is opened for appending ONLY as there should be no other
            # operation other than reading (for the weeding module) that should be
            # occurring with the file.

            g.write("Book with ID " + book_id + " was returned on: "
                    + CURRENT_DATE_TIME.strftime("%d/%m/%Y") + "." + "\n")
            # This like will then paste the line above which would look like
            # "Book with ID 1 was returned on: 14/12/2020" followed by
            # a new line for the next entry.
            g.close()
            # The file is then closed to avoid the next line printing back into
            # the logfile.

        print("Book with ID " + book_id + " was returned on: "
              + CURRENT_DATE_TIME.strftime("%d/%m/%Y") + "." + "\n")
        # The program will then print the same message to the user.


#  TEST CODE
# Below are variables you can enter into this module in order to receive an
# output followed by a test selection.

if __name__ == "__main__":
    #  CODE 1 - Valid Data
    # Input = "1"

    print("TEST: CODE 1")
    book_id = "1"
    book_return(book_id)

# Expected Output =
# "Book with ID 1 was returned at: Day Month Date hr:min:sec Year"
# Database entry matching book_id 1 will have the member_id changed to 0 to
# indicate that it has been returned and ready to be checked out.
# New logfile.txt entry which reads Book with ID 1 was returned at:
# Day/Month/Year.


# CODE 2 - Valid Data Type however value does not exist within the database
# Input = "x" where x is any number outside the range of 1 =< x <= 10
# (i.e., -1 or 50)
    print("TEST: CODE 2a")
    book_id = "-1"
    book_return(book_id)

    print("TEST: CODE 2b")
    book_id = "11"
    book_return(book_id)

# Expected Output = "ERROR: Book not found!"

#  CODE 3 - Invalid Data
# Input = Book

    print("TEST: CODE 3")
    book_id = "Book"
    book_return(book_id)

# Expected Output = "ERROR: Book not found!"

#  CODE 4 - Null Value
# Input = ''

    print("TEST: CODE 4")
    book_id = ""
    book_return(book_id)

# Expected Output = "ERROR: Book not found!"
