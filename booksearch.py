import csv

# I have imported CSV to make use of CSV functionality within the .txt based
# database


def book_search(book_title):
    # This functions serves to look up the title entered by the user in the book
    # database and produce an output containing the matching books and their
    # details.

    if __name__ == "booksearch":
        # This selection is to prevent the code from being run when imported
        # but only to run when called upon as seen in the testing section of
        # this module or the menu module.

        with open('database.txt', 'r') as csv_file:
            # The database file is opened for reading. This is so the inputs
            # can be compared to the elements stored in the database.

            csv_reader = csv.DictReader(csv_file)
            # Variable called 'csv_reader' contains the function which reads
            # the file as a Dictionary Reader so that the headers can be taken
            # into account when comparing input to the database.

            for line in csv_reader:
                # This for loop iterates for every line that appears
                # in csv_reader.

                if book_title == line['title']:
                    # Here the code reads all of the lines in csv_reader
                    # matches the title column and checks every book title that
                    # appears in this column books and matches the ones with
                    # an identical name.

                    for identifier, value in line.items():
                        # Here a format is introduced so that each of the
                        # matching rows are formatted in a more readable way.

                        print(identifier, ':', value)

                        # And then printed in a format similar to "book_id : 1"
                        # with the rest of the headers and elements following
                        # this style.
            else:
                print("ERROR: Book not found!")
                # An otherwise clause which executes if the book title does not
                # match an acceptable format producing this error message.


#  TEST CODE
#  Below are variables you can enter into this module in order to receive an
#  output.

if __name__ == '__main__':

#  CODE 1 - Valid Data
# Input = "Book_1"

    print("TEST: CODE 1")
    book_title = "Book_1"
    book_search(book_title)

# Expected Output =
# "book_id : 1
# isbn : 9783161484100
# title : Book_1
# author : Author_1
# purchase_date : 20/4/2006
# member_id : 0
# book_id : 4
# isbn : 9783161484100
# title : Book_1
# author : Author_1
# purchase_date : 20/4/2006
# member_id : 1234
# book_id : 6
# isbn : 9783161484100
# title : Book_1
# author : Author_1
# purchase_date : 20/4/2006
# member_id : 1244"

#  CODE 2 - Valid Data Type however value does not exist within the database
# Input = "Book_x" where x is any number outside the range of
# 1 =< x <= 4 (i.e., Book_-1 or Book_5)
    print("TEST: CODE 2a")
    book_title = "Book_-1"
    book_search(book_title)

    print("TEST: CODE 2b")
    book_title = "Book_5"
    book_search(book_title)

# Expected Output = "ERROR: Book not found!"

#  CODE 3 - Invalid Data
# Input = 4

    print("TEST: CODE 3")
    book_title = 4
    book_search(book_title)

# Expected Output = "ERROR: Book not found!"

#  CODE 4 - Null Value
# Input = ''

    print("TEST: CODE 4")
    book_title = ""
    book_search(book_title)

# Expected Output = "ERROR: Book not found!"



