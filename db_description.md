My is database is designed to manage a library system. It consists of several interrelated tables, each serving a specific purpos in storing and organizing library data. 

Tables and Attributes: 

    Books: 
        Attributes: BookID (INT), Title (VARCHAR(100)), Genre (VARCHAR(50)), Language(VARCHAR(50)) 
        Primary Key: BookID
        Sample Data: 
            (1, '1984', 'Dystopian', 'English')
            (2, 'Harry Potter and the Sorcerer's Stone', 'Fantasy', 'English')

    Authors: 
        Attributes: AuthorID (INT), FirstName(VARCHAR(50)), LastName(VARCHAR(50)), BirthDate(DATE)
        Primary Key: AuthorID
        Sample Date: 
            (1, 'George', 'Orwell' '1903-06-25')
            (2, 'J.K', 'Rowling', '1965-07-31')

    BookAuthors:
        Attributes: BookAuthorID (INT), BookID(INT), AuthorID (INT), Contribution (VARCHAR(100)), ISBN (VARCHAR(13))
        Primary Key: BookAuthorID
        Foreign Keys: BookID (references Books), AuthorID (references Authors)
        Sample Data: 
            (1,1,1, 'Author', '9780451524935')
            (2,2,2, 'Author', '9780590353427')

    Publishers: 
        Attributes: PubslisherID (INT), PublisherName (VARCHAR(100)), Address (VARCHAR(255)), Phone (VARCHAR(15))
        Primary Key: PublisherID
        Sample Data: 
            (1, 'Penguin Random House', '123 Main St, New York', '555-123-4567')
            (2, 'Harper Collins', '456 Elm St, London' '44-20-5555-5555)

    BookPublishers: 
        Attributes: BookPublisherID (INT), BookID (INT), PublisherID(INT), PublicationDate (Date), Edition (VARCHAR(20))
        Primary Key: BookPublisherID
        Foreign Key: BookID (references Books), PublisherID (references Publishers)
        Sample Data: 
            (1,1,1,'1949-06-08' '1st')
            (2,2,2, '1997-06-26', '1st')

    Patrons: 
        Attributes: PatronID (INT), FirstName (VARCHAR(50)), LastName (VARCHAR(50)), Email (VARCHAR(100))
        Primary Key: PatronID 
        Sample Data: 
            (1, 'John', 'Doe', 'johndoe@example.com')
            (2, 'Jane', 'Smith', 'janesmith@example.com')


Foreign Key Constraints: 

    BookAuthors: 
        'FK_BookID_Authors' ensures 'BookID' in 'BookAuthors' references a valid 'BookID' in 'Books' 
        'Fk_AuthorID' ensures 'AuthorID' in 'BookAuthors' references a valid 'AuthorID' in 'Authors' 

    BookPublishers: 
        'FK_BookID_Publishers' ensures 'BookID' in 'BookPublishers' references a valid 'BookID' in 'Books' 
        'FK_PublisherID' ensures 'PublisherID' in 'BookPublishers' references a valid 'PublisherID' in 'Publishers' 

    Functional Dependencies (FDs): 
        Books: BookID -> Title, Genre, Language
        Authors: AuthorID -> Firstname, LastName, BirthDate
        BookAuthors: BookAuthorID -> BookID, AuthorID, Contribution, ISBN
                     BookID -> ISBN 
                     AuthorID -> Contribution 
        Publishers: PublisherID -> PublisherName, Address, Phone
        BookPublishers: BookPublisherID -> BookID, PublisherID, PublicationDate, Edition
                        BookID -> Edition, PublicationDate
        Patrons: PatronID -> FirstName, LastName, Email

Normalization and 3NF: 
    Each table has a primary key which ensures uniquenss
    all attributes are dependent only on the primary key, fulfilling the requirement of 1NF
    There are no partail dependencies of any attribute on a key, satisfying 2NF
    There are no transitive dependencies, meeting 3NF requirements 
    This structure minimizes redundany and ensures data integrity, making it a good system for a library management system 