Command line/Text-based UI

To use the program the user must execute 'menu.py' and make use of the text
user interface (TUI) in order to make use of the system.

The program will ask the user to choose a function to use, followed by 4
different options 'bs' - for the book searching function, 'bc' - for the book
checkout function, 'br' - for the book returning function and finally 'ex' -
the exit function to terminate the program prematurely.

The 'bs' function will ask for a single input from the user - a book name.
The input will need to match a book title otherwise the system will output
an error message. Acceptable inputs are the following strings; "Book_1" ,
"Book_2" , "Book_3" , "Book_4".

The 'bc' function will ask for two inputs from the user - a book ID and a
member ID in order to check out the book. The input will need to match an
acceptable book ID and member ID otherwise the system will output an error
message. Acceptable inputs are the following; "1" and "9827".

Finally, The 'br' function will ask for a single input from the user - a
book ID. The input will need to match an acceptable book ID otherwise the system
will incorrectly accept the input but will not update the database however it
will incorrectly and print log a successful return. Acceptable inputs are
numbers from 1-10.

I was unable to get tkinter working in the way I wanted to so I have not made
use of the tkinter library nor the matplotlib library. Therefore, the GUI serves
no functional purpose and does not work properly, the same applies to the
database.py and bookweed.py files.

Lastly, in order to use the tests simply run each module individually for an
output.
