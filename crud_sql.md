1) Create (I created three predefined statements that create 3 new entries into the database tables)
    
    INSERT INTO Books (BookID, Title, Genre, Language) 
    VALUES (6, 'The Catcher in the Rye', 'Fiction', 'English')

    INSERT INTO Publishers (PublisherID, PublisherName, Address, Phone) 
    VALUES (6, 'Random House', '321 Elm St, Boston', '555-987-6543')

    INSERT INTO Patrons (PatronID, FirstName, LastName, Email) 
    VALUES (6, 'Emily', 'Johnson', 'emilyjohnson@example.com');

2) Read (I have three read statments that show all the info in 3 tables)

    SELECT Title, Genre, Language 
    FROM Books;

    SELECT PublisherName, Address, Phone 
    FROM Publishers; 

    SELECT FirstName, LastName, Email 
    FROM Patrons;

3) Update ( I created 3 statments that update information in the tables as follows)

    UPDATE Books SET Title = 'New Title' 
    WHERE BookID = 6

    UPDATE Publishers SET Address = 'New Address' 
    WHERE PublisherID = 6;

    UPDATE Patrons SET LastName = 'New Name' 
    WHERE PatronID = 6;

4) Delete (3 statments that delete info from the database)

    DELETE FROM Books 
    WHERE BookID = 6;

    DELETE FROM Publishers 
    WHERE PublisherID = 6;

    DELETE FROM Patrons 
    WHERE PatronID = 6;

These statments create, update, and delete the same information from the database and the read statments show that tables that have been changed. 