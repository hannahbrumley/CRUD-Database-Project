CREATE DATABASE lib_database_system;


CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100),
    Genre VARCHAR(50),
    Language VARCHAR(50)
);
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE
);

CREATE TABLE BookAuthors (
    BookAuthorID INT PRIMARY KEY,
    BookID INT,
    AuthorID INT,
    Contribution VARCHAR(100), -- Additional field for author's contribution
    ISBN VARCHAR(13), -- Additional field for ISBN if needed
    CONSTRAINT FK_BookID_Authors FOREIGN KEY (BookID) REFERENCES Books(BookID),
    CONSTRAINT FK_AuthorID FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);
CREATE TABLE Publishers (
    PublisherID INT PRIMARY KEY,
    PublisherName VARCHAR(100),
    Address VARCHAR(255),
    Phone VARCHAR(15)
);
CREATE TABLE BookPublishers (
    BookPublisherID INT PRIMARY KEY,
    BookID INT,
    PublisherID INT,
    PublicationDate DATE, -- Additional field for publication date
    Edition VARCHAR(20), -- Additional field for edition if needed
    CONSTRAINT FK_BookID_Publishers FOREIGN KEY (BookID) REFERENCES Books(BookID),
    CONSTRAINT FK_PublisherID FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID)
);

CREATE TABLE Patrons (
    PatronID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100)
);
