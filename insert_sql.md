INSERT INTO Authors (AuthorID, FirstName, LastName, BirthDate)
VALUES
    (1, 'George', 'Orwell', '1903-06-25'),
    (2, 'J.K.', 'Rowling', '1965-07-31'),
    (3, 'Harper', 'Lee', '1926-04-28'),
    (4, 'F. Scott', 'Fitzgerald', '1896-09-24'),
    (5, 'Agatha', 'Christie', '1890-09-15');


INSERT INTO Publishers (PublisherID, PublisherName, Address, Phone)
VALUES
    (1, 'Penguin Random House', '123 Main St, New York', '555-123-4567'),
    (2, 'HarperCollins', '456 Elm St, London', '44-20-5555-5555'),
    (3, 'Simon & Schuster', '789 Oak St, San Francisco', '415-555-7890'),
    (4, 'Hachette Livre', '101 Maple Ave, Paris', '33-1-5555-5555'),
    (5, 'Macmillan Publishers', '246 Birch Rd, Toronto', '416-555-2468');


INSERT INTO Books (BookID, Title, Genre, Language)
VALUES
    (1, '1984', 'Dystopian', 'English'),
    (2, 'Harry Potter and the Sorcerer''s Stone', 'Fantasy', 'English'),
    (3, 'To Kill a Mockingbird', 'Fiction', 'English'),
    (4, 'The Great Gatsby', 'Classics', 'English'),
    (5, 'Murder on the Orient Express', 'Mystery', 'English');


INSERT INTO BookAuthors (BookAuthorID, BookID, AuthorID, Contribution, ISBN)
VALUES
    (1, 1, 1, 'Author', '9780451524935'),
    (2, 2, 2, 'Author', '9780590353427'),
    (3, 3, 3, 'Author', '9780061120084'),
    (4, 4, 4, 'Author', '9780743273565'),
    (5, 5, 5, 'Author', '9780062073501');


INSERT INTO BookPublishers (BookPublisherID, BookID, PublisherID, PublicationDate, Edition)
VALUES
    (1, 1, 1, '1949-06-08', '1st'),
    (2, 2, 2, '1997-06-26', '1st'),
    (3, 3, 3, '1960-07-11', '1st'),
    (4, 4, 4, '1925-04-10', '1st'),
    (5, 5, 5, '1934-01-01', '1st');


INSERT INTO Patrons (PatronID, FirstName, LastName, Email)
VALUES
    (1, 'John', 'Doe', 'johndoe@example.com'),
    (2, 'Jane', 'Smith', 'janesmith@example.com'),
    (3, 'David', 'Brown', 'davidbrown@example.com'),
    (4, 'Susan', 'Johnson', 'susanjohnson@example.com'),
    (5, 'Michael', 'Wilson', 'michaelwilson@example.com');
