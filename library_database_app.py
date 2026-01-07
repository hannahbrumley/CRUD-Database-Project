import tkinter as tk
from tkinter import ttk
import mysql.connector

# Function to create a new book entry
def create_book():
    cursor = db.cursor()
    query = "INSERT INTO Books (BookID, Title, Genre, Language) VALUES (6, 'The Catcher in the Rye', 'Fiction', 'English');"
    cursor.execute(query)
    db.commit()
    
    # Fetch the inserted data
    cursor.execute("SELECT * FROM Books WHERE BookID = 6;")
    result = cursor.fetchone()
    
    cursor.close()
    
    if result:
        output_text.set("New book entry created:\n")
        output_text.set(output_text.get() + f"BookID: {result[0]}\nTitle: {result[1]}\nGenre: {result[2]}\nLanguage: {result[3]}\n")
        print("New book entry created.")

# Function to create a new publisher entry
# Function to create a new publisher entry
def create_publisher():
    try:
        cursor = db.cursor()
        query = "INSERT INTO Publishers (PublisherID, PublisherName, Address, Phone) VALUES (6, 'Random House', '321 Elm St, Boston', '555-987-6543');"
        cursor.execute(query)
        db.commit()
    
        # Fetch the inserted data
        cursor.execute("SELECT * FROM Publishers WHERE PublisherID = 6;")
        result = cursor.fetchone()
    
        cursor.close()
    
        if result:
            output_text.set("New publisher entry created:\n")
            output_text.set(output_text.get() + f"PublisherID: {result[0]}\nPublisherName: {result[1]}\nAddress: {result[2]}\nPhone: {result[3]}\n")
            print("New publisher entry created.")
    except Exception as e:
        output_text.set(f"Error creating publisher entry: {str(e)}")
        print("Error creating publisher entry:", e)


# Function to create a new patron entry
def create_patron():
    cursor = db.cursor()
    query = "INSERT INTO Patrons (PatronID, FirstName, LastName, Email) VALUES (6, 'Emily', 'Johnson', 'emilyjohnson@example.com');"
    cursor.execute(query)
    db.commit()
    
    # Fetch the inserted data
    cursor.execute("SELECT * FROM Patrons WHERE PatronID = 6;")
    result = cursor.fetchone()
    
    cursor.close()
    
    if result:
        output_text.set("New patron entry created:\n")
        output_text.set(output_text.get() + f"PatronID: {result[0]}\nFirstName: {result[1]}\nLastName: {result[2]}\nEmail: {result[3]}\n")
        print("New patron entry created.")

# Function to read book information
def read_books():
    cursor = db.cursor()
    query = "SELECT Title, Genre, Language FROM Books;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    output_text.set("Book Information:\n")
    for row in result:
        output_text.set(output_text.get() + f"{row}\n")
    print("Read book information.")

# Function to read publisher information
def read_publishers():
    cursor = db.cursor()
    query = "SELECT PublisherName, Address, Phone FROM Publishers;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    output_text.set("Publisher Information:\n")
    for row in result:
        output_text.set(output_text.get() + f"{row}\n")
    print("Read publisher information.")

# Function to read patron information
def read_patrons():
    cursor = db.cursor()
    query = "SELECT FirstName, LastName, Email FROM Patrons;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    output_text.set("Patron Information:\n")
    for row in result:
        output_text.set(output_text.get() + f"{row}\n")
    print("Read patron information.")

# Function to update a book entry
def update_book():
    cursor = db.cursor()
    query = "UPDATE Books SET Title = 'New Title' WHERE BookID = 6;"
    cursor.execute(query)
    db.commit()
    cursor.close()
    output_text.set("Book entry updated.")
    print("Book entry updated.")

#Function to update a publisher entry
def update_publisher(): 
    cursor = db.cursor()
    query = "UPDATE Publishers SET Address = 'New Address' WHERE PublisherID = 6;"
    cursor.execute(query)
    db.commit()
    cursor.close()
    output_text.set("Publisher entry updated.")
    print("Publisher entry updated.")

#Function to update patron entry
def update_patron():
    cursor = db.cursor()
    query = "UPDATE Patrons SET LastName = 'New Name' WHERE PatronID = 6;"
    cursor.execute(query)
    db.commit()
    cursor.close()
    output_text.set("Patron entry updated.")
    print("Patron entry updated.")

# Function to delete a book entry
def delete_book():
    cursor = db.cursor()
    query = "DELETE FROM Books WHERE BookID = 6;"
    cursor.execute(query)
    db.commit()
    cursor.close()
    output_text.set("Book entry deleted.")
    print("Book entry deleted.")

#delete Publisher entry
def delete_Publisher():
    cursor = db.cursor()
    query = "DELETE FROM Publishers WHERE PublisherID = 6;"
    cursor.execute(query)
    db.commit()
    cursor.close()
    output_text.set("Publisher entry deleted. ")
    print("Publisher entry deleted. ")

#delete Patron entry 
def delete_Patron(): 
    cursor = db.cursor()
    query = "DELETE FROM Patrons WHERE PatronID = 6;"
    cursor.execute(query)
    db.commit()
    cursor.close()
    output_text.set("Patron entry deleted.")
    print("Patron entry deleted.")


#Retrieve a list of books with their authors' names
def list_books_with_authors():
    cursor = db.cursor()
    query = """
    SELECT b.Title AS BookTitle, CONCAT(a.FirstName, ' ', a.LastName) AS AuthorName
    FROM Books AS b
    JOIN BookAuthors AS ba ON b.BookID = ba.BookID
    JOIN Authors AS a ON ba.AuthorID = a.AuthorID;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    output_text.set("List of Books with Authors:\n")
    for row in result:
        output_text.set(output_text.get() + f"{row}\n")
    print("List of books with authors generated.")

#Find the books published by a specific publisher
def books_published_by_publisher():
    cursor = db.cursor()
    query = """
    SELECT b.Title AS BookTitle, p.PublisherName
    FROM Books AS b
    JOIN BookPublishers AS bp ON b.BookID = bp.BookID
    JOIN Publishers AS p ON bp.PublisherID = p.PublisherID
    WHERE p.PublisherName = 'Penguin Random House';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    
    # Clear the existing output_text
    output_text.set("")
    
    # Prepare a string to display the result
    output_str = "Books published by Penguin Random House:\n"
    for row in result:
        output_str += f"Title: {row[0]}, Publisher: {row[1]}\n"
    
    # Update the output_text with the new content
    output_text.set(output_str)
    print("Books published by Penguin Random House generated.")


#Count the number of books authored by each author
def count_books_by_author():
    cursor = db.cursor()
    query = """
    SELECT CONCAT(a.FirstName, ' ', a.LastName) AS AuthorName, COUNT(*) AS BookCount
    FROM Authors AS a
    JOIN BookAuthors AS ba ON a.AuthorID = ba.AuthorID
    GROUP BY a.AuthorID;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    output_text.set("Books Count by Author:\n")
    for row in result:
        output_text.set(output_text.get() + f"{row}\n")
    print("Books count by author generated.")

#Get a list of books (titles) published by a particular author
def book_titles_by_author():
    cursor = db.cursor()
    query = """
    SELECT Books.Title
    FROM Books
    INNER JOIN BookAuthors ON Books.BookID = BookAuthors.BookID
    INNER JOIN Authors ON BookAuthors.AuthorID = Authors.AuthorID
    WHERE Authors.FirstName = 'George' AND Authors.LastName = 'Orwell'
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    output_text.set("Titles by George Orwell: \n")
    for row in result: 
        output_text.set(output_text.get() + f"{row}\n")
    print("Titles by Author")

# Create the main window
root = tk.Tk()
root.title("Library Database System")

# Connect to your MySQL database
db = mysql.connector.connect(
    host="#######",
    user="#####",
    password="#######",
    database="lib_database_system"
)

# Create buttons
create_book_button = ttk.Button(root, text="Create Book", command=create_book)
create_publisher_button = ttk.Button(root, text="Create Publisher", command=create_publisher)
create_patron_button = ttk.Button(root, text="Create Patron", command=create_patron)
read_books_button = ttk.Button(root, text="Read Books", command=read_books)
read_publishers_button = ttk.Button(root, text="Read Publishers", command=read_publishers)
read_patrons_button = ttk.Button(root, text="Read Patrons", command=read_patrons)
update_book_button = ttk.Button(root, text="Update Book", command=update_book)
update_publisher_button = ttk.Button(root, text="Update Publisher", command=update_publisher)
update_patron_button = ttk.Button(root, text="Update Patron", command = update_patron)
delete_book_button = ttk.Button(root, text="Delete Book", command=delete_book)
delete_publisher_button = ttk.Button(root, text="Delete Publisher", command= delete_Publisher)
delete_patron_button = ttk.Button(root, text="Delete Patron", command = delete_Patron)
book_author_table_button = ttk.Button(root, text="Book and Author Table", command = list_books_with_authors)
books_published_by_publisher_button = ttk.Button(root, text="Books by Publisher", command= books_published_by_publisher)
count_books_by_author_button = ttk.Button(root, text="Count of Books by Author", command = count_books_by_author)
book_titles_by_author_button = ttk.Button(root, text = "Titles by Author", command = book_titles_by_author)
# Create an output label
output_text = tk.StringVar()
output_label = ttk.Label(root, textvariable=output_text)

# Arrange widgets
create_book_button.pack()
create_publisher_button.pack()
create_patron_button.pack()
read_books_button.pack()
read_publishers_button.pack()
read_patrons_button.pack()
update_book_button.pack()
update_publisher_button.pack()
update_patron_button.pack()
delete_book_button.pack()
delete_publisher_button.pack()
delete_patron_button.pack()
book_author_table_button.pack()
books_published_by_publisher_button.pack()
count_books_by_author_button.pack()
book_titles_by_author_button.pack()
output_label.pack()

root.mainloop()
