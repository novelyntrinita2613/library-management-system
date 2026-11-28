# Establishing connection between python and mysql
import os
import mysql.connector as mys
from mysql.connector import Error

mycon = ""
mycursor = ""

# Database configuration. Set these environment variables on your computer
# or edit the defaults below to match your local MySQL installation.
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "krithika07")
DB_NAME = os.getenv("DB_NAME", "librarymanagement")

# Creating database for the library
def create_database():
    connection = mys.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
    connection.commit()
    cursor.close()
    connection.close()


# Using the database "librarymanagement"
def get_connection():
    return mys.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


# Creating the table "books"
def create_books():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            bookname VARCHAR(50),
            authorname VARCHAR(50),
            copies INT,
            bookid VARCHAR(50) PRIMARY KEY
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()


# Creating the table "borrow"
def create_borrow():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrow (
            bookname VARCHAR(50),
            authorname VARCHAR(50),
            borrowdate DATE,
            duedate DATE,
            name VARCHAR(50),
            id VARCHAR(50)
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()


# Creating the table "membership"
def create_membership():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS membership (
            member_id INT PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50),
            phonenumber BIGINT,
            count INT,
            membership VARCHAR(50)
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()


# Creating the table "return_book"
def create_return_book():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS return_book (
            name VARCHAR(50),
            bookname VARCHAR(50),
            returndate DATE,
            status VARCHAR(50),
            member_id INT
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()


def create_tables():
    create_books()
    create_borrow()
    create_membership()
    create_return_book()


# Creating the login page
def login():
    global mycon
    global mycursor

    try:
        mycon = get_connection()
        mycursor = mycon.cursor()

        a = input("Enter username: ")
        b = input("Enter password: ")

        if b == "novakiki#2122":
            print("ACCESS GRANTED!")
            print("""
------------------------------------------------------------------------------------------------
                                      BOOK LOVERS CLUB
------------------------------------------------------------------------------------------------
""")
            print("WELCOME TO LIBRARY MANAGEMENT SYSTEM")
            menu(mycursor)
        else:
            print("Wrong password......try again")
    finally:
        if mycursor and mycursor != "":
            mycursor.close()
        if mycon and mycon != "":
            mycon.close()


# Creating the menu
def menu(mycursor):
    while True:
        print("\nMenu:")
        print("1. Add a Book")
        print("2. Add a member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Viewing available books")
        print("6. Searching available books")
        print("7. Viewing already existing members of the library")
        print("8. Searching for an already existing member")
        print("9. Delete a book")
        print("10. Delete a membership")
        print("11. Exit")

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice, please try again.")
            continue

        if ch == 1:
            add_book(mycursor)
            books_file(mycursor)
            break
        elif ch == 2:
            add_member(mycursor)
            members_file(mycursor)
            break
        elif ch == 3:
            borrow_book(mycursor)
            borrow_file(mycursor)
            break
        elif ch == 4:
            return_book(mycursor)
            return_file(mycursor)
            break
        elif ch == 5:
            view_books(mycursor)
            break
        elif ch == 6:
            search_books(mycursor)
            break
        elif ch == 7:
            view_members(mycursor)
            break
        elif ch == 8:
            search_members(mycursor)
            break
        elif ch == 9:
            delete_book(mycursor)
            books_file(mycursor)
            break
        elif ch == 10:
            delete_member(mycursor)
            members_file(mycursor)
            break
        elif ch == 11:
            break
        else:
            print("Invalid choice, please try again.")


# To add a new book
def add_book(mycursor):
    bookname = input("Enter the book name: ")
    authorname = input("Enter the author name: ")
    copies = int(input("Enter the number of copies: "))
    bookid = input("Enter the book id: ")

    mycursor.execute(
        "INSERT INTO books (bookname, authorname, copies, bookid) VALUES (%s, %s, %s, %s)",
        (bookname, authorname, copies, bookid)
    )
    mycon.commit()
    print("New book added successfully!")


# To display the addition in a text file
def books_file(mycursor):
    with open("books.txt", "w", encoding="utf-8") as f:
        mycursor.execute("SELECT * FROM books")
        x = mycursor.fetchall()
        for record in x:
            f.write(str(record) + "\n")
    print("Data written to books.txt successfully!")


# To add a new membership
def add_member(mycursor):
    mid = int(input("Enter membership id: "))
    name = input("Enter member name: ")
    em = input("Enter email: ")
    phno = int(input("Enter phone number: "))
    count = int(input("Enter the number of times borrowed: "))
    membership = input("Enter membership status: ")
    values = (mid, name, em, phno, count, membership)

    mycursor.execute(
        "INSERT INTO membership (member_id, name, email, phonenumber, count, membership) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        values
    )
    mycon.commit()
    print("New member added successfully!")


# To display the addition in a text file
def members_file(mycursor):
    with open("members.txt", "w", encoding="utf-8") as f:
        mycursor.execute("SELECT * FROM membership")
        x = mycursor.fetchall()
        for record in x:
            f.write(str(record) + "\n")
    print("Data written to members.txt successfully!")


# To enter details of a borrowal
def borrow_book(mycursor):
    book = input("Enter book that is being borrowed: ")
    author = input("Enter author name: ")
    date = input("Enter date of borrowing (YYYY-MM-DD): ")
    due = input("Enter due date (YYYY-MM-DD): ")
    name = input("Enter name of the member: ")
    ID = int(input("Enter member id: "))
    values = (book, author, date, due, name, ID)

    mycursor.execute(
        "INSERT INTO borrow (bookname, authorname, borrowdate, duedate, name, id) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        values
    )
    mycon.commit()
    print("Borrow status updated successfully!")


# To display the addition in a text file
def borrow_file(mycursor):
    with open("borrow.txt", "w", encoding="utf-8") as f:
        mycursor.execute("SELECT * FROM borrow")
        x = mycursor.fetchall()
        for record in x:
            f.write(str(record) + "\n")
    print("Data written to borrow.txt successfully!")


# To enter details of a return
def return_book(mycursor):
    name = input("Enter name of the member: ")
    book = input("Enter book name: ")
    date = input("Enter date of return (YYYY-MM-DD): ")
    status = input("Enter borrow status: ")
    ID = int(input("Enter member id: "))
    values = (name, book, date, status, ID)

    mycursor.execute(
        "INSERT INTO return_book (name, bookname, returndate, status, member_id) "
        "VALUES (%s, %s, %s, %s, %s)",
        values
    )
    mycon.commit()
    print("Return status updated successfully!")


# To display the addition in a text file
def return_file(mycursor):
    with open("return.txt", "w", encoding="utf-8") as f:
        mycursor.execute("SELECT * FROM return_book")
        x = mycursor.fetchall()
        for record in x:
            f.write(str(record) + "\n")
    print("Data written to return.txt successfully!")


# To view all the available books
def view_books(mycursor):
    mycursor.execute("SELECT * FROM books")
    result = mycursor.fetchall()
    for record in result:
        print(record)


# To search a book
def search_books(mycursor):
    bookname = input("Enter name of the book: ")
    authorname = input("Enter name of author: ")
    sql = "SELECT * FROM books WHERE bookname = %s AND authorname = %s"
    values = (bookname, authorname)
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()

    if myresult:
        for x in myresult:
            print(x)
    else:
        print("No such book found")


# To view all the existing members
def view_members(mycursor):
    mycursor.execute("SELECT * FROM membership")
    result = mycursor.fetchall()
    for record in result:
        print(record)


# To search a member
def search_members(mycursor):
    member_id = int(input("Enter id of the member: "))
    name = input("Enter name of the member: ")
    sql = "SELECT * FROM membership WHERE member_id = %s AND name = %s"
    values = (member_id, name)
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()

    if myresult:
        for x in myresult:
            print(x)
    else:
        print("No such member found")


# To delete details of a book
def delete_book(mycursor):
    bookname = input("Enter the book name :")
    bookid = input("Enter the book id :")
    mycursor.execute(
        "DELETE FROM books WHERE bookname = %s AND bookid = %s",
        (bookname, bookid)
    )
    mycon.commit()
    if mycursor.rowcount:
        print("Book deleted successfully!!!!!")
    else:
        print("No such book found")


# To delete details of a membership
def delete_member(mycursor):
    name = input("Enter the member name :")
    mid = input("Enter the member id :")
    mycursor.execute(
        "DELETE FROM membership WHERE name = %s AND member_id = %s",
        (name, mid)
    )
    mycon.commit()
    if mycursor.rowcount:
        print("Membership deleted successfully!!!!!")
    else:
        print("No such member found")


# Creating the database and tables, then starting the application
if __name__ == "__main__":
    try:
        create_database()
        create_tables()
        login()
    except Error as error:
        print("Database error:", error)
        print("Check that MySQL is running and your database settings are correct.")
    except ValueError:
        print("Invalid input. Please enter a valid number where required.")
