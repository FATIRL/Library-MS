import csv
import fileinput
import datetime

# Imported CSV to make use of CSV functionality within the .txt based database.
# Imported datetime to make use dates and times with the intention to be used
# in the weeding module.
# Imported fileinput in order to make changes to the database in real time
# without having to manually handle files.

CURRENT_DATE_TIME = datetime.datetime.now()

# This global constant is made for the logfile.txt and weeding module as a
# way to keep track of when books are being checked out and returned.

CURRENT_BOOK_IDs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# I also made a list which serves as a constant which contains all of the unique
# book IDs that exist in the database to eliminate the need for data handling
# within the function.



def book_checkout(book_id, member_id, member_id_int):
    # This function serves as the method to check books out of the system
    # given a book_id and member_id. The third variable is used to make a
    # comparison a few lines down.

    if __name__ == "bookcheckout":
        # This selection is to prevent the code from being run when imported
        # but only to run when called upon as seen in the testing section of
        # this module or the menu module.

        if len(member_id) != 4 or member_id_int <= 1000 or book_id not in CURRENT_BOOK_IDs:
            # As such, the length function is used to make sure that the
            # member_id is not too long (i.e., a 5 digit number such a 12345)
            # and also make sure it is not less than 1000 (i.e., a 4 digit
            # number less than 1000 would be 0003). If this statement returns
            # as true then an error message will be produced.
            print("ERROR: This is an invalid book and/or member ID!")

        else:
            # As an otherwise clause the following executes

            with fileinput.input(files='database.txt', inplace=True, mode='r') as f:
                # This function the fileinput module is used to replace lines
                # in the database.txt without having to handle multiple
                # versions of this file in real time.

                reader = csv.DictReader(f)
                # Again the variable called 'csv_reader' contains the
                # function which reads the file as a Dictionary Reader so that
                # the headers can be taken into account when comparing input to
                # the database.

                print(",".join(reader.fieldnames))
                #  Again the code is to use "," as the limiter and using the
                #  DictReader print the field names or headers back into the
                #  database file.

                for row in reader:
                    # This for loop iterates for every row that appears in
                    # csv_reader.

                    if book_id == row["book_id"]:
                        #  This selection statement check to see if the line it
                        #  is currently iterating matches the user input for
                        #  the "book_id".

                        row['member_id'] = member_id
                        # then the currently held value for "member_id" in the
                        # database is set to the user's input.

                    print(",".join([row["book_id"], row["isbn"], row["title"],
                                    row["author"], row["purchase_date"],
                                    row["member_id"]]))
                    # It then prints the values it has read back into the file
                    # with the updated information (if any). The following code
                    # was to be used as functionality which supports the
                    # logfile.txt and the weeding.py module.

    f = open("logfile.txt", "a")
    #  Here the file is opened for appending ONLY as there should be no
    #  other operation other than reading (for the weeding module) that should
    #  be occurring with the file.

    f.write("Book with ID " + book_id + " was checked out on: "
            + CURRENT_DATE_TIME.strftime("%d/%m/%Y") + " by member with ID "
            + member_id + "." + "\n")
    #  This like will then paste the line above which would look like
    #  "Book with ID 1 was checked out on: 14/12/2020 by member with ID 1242."
    #  followed by a new line for the next entry.

    f.close()
    #  The file is then closed to avoid the next line printing back into the
    #  logfile.

    print("Book with ID " + book_id + " was checked out on: "
          + CURRENT_DATE_TIME.strftime("%d/%m/%Y") + " by member with ID "
          + member_id + ".")
    # And the same is printed out to the user.


#  TEST CODE
# Below are variables you can enter into this module in order to receive
# an output.

if __name__ == '__main__':
    #  CODE 1 - Valid Data

    # Input1 = "x" where x is part of the book_ids/CURRENT_BOOK_IDs
    # Input2 = "y" where y is any 4-digit number that satisfies the selection
    # condition if len(member_id) != 4 or member_id_int <= 1000
    # Essentially any number y where: 999 < y < 10000

    print("TEST: CODE 1")
    book_id = '4'
    member_id = '2415'
    member_id_int = int(member_id)
    book_checkout(book_id, member_id, member_id_int)

    # Expected Output =
    # The program should print a message:
    # "Book with {Input1} was checked out at: Day Month Date hh:mm:ss yyyy by
    # member with {Input2}." Followed by the corresponding line that matches
    # {Input1} in the database having the member_id changed to {Input2}
    # Lastly the line Book with ID {Input1} was checked out at: dd/mm/yyyy by
    # member with ID {Input2}.

    #  CODE 2 - Valid Data Type however value does not exist within the database

    # Either an 'out of range' Input1 or Input2 will generate an error here.
    # Input1 = "x" is any number y where: 1 < x  or x > 10 (i.e., -1 or 11)
    # Input2 = "y" is any number y where: 1000 > y or y > 9999
    # (i.e., 999 or 10000)

    print("TEST: CODE 2a")
    book_id = '242356'
    member_id = '2415'
    member_id_int = int(member_id)
    book_checkout(book_id, member_id, member_id_int)

    print("TEST: CODE 2b")
    book_id = '4'
    member_id = '322415'
    member_id_int = int(member_id)
    book_checkout(book_id, member_id, member_id_int)

    # Expected Output = "ERROR: This is an invalid book and/or member ID!"

    #  CODE 3 - Invalid Data
    # Input1 = Any string/char etc.
    # and/or
    # Input2 = Any string/char etc.

    print("TEST: CODE 3")
    book_id = 'Hello'
    member_id = '2415'
    member_id_int = int(member_id)
    book_checkout(book_id, member_id, member_id_int)

    # Expected Output = "ERROR: This is an invalid book and/or member ID!"

    #  CODE 4 - Null Value
    # Input1 = ''
    # and/or
    # Input2 = ''

    print("TEST: CODE 4")
    book_id = ''
    member_id = ''
    member_id_int = int(member_id)
    book_checkout(book_id, member_id, member_id_int)

# Expected Output = "ERROR: This is an# invalid book and/or member ID!"
