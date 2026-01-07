# CRUD Database Project (Library Database)

Simple Python/Tkinter CRUD app for a library-style database. This repo contains SQL for creating and populating a sample library schema plus a small desktop GUI that demonstrates create, read, update, delete and a few reporting queries.

What’s in the repo
- library_database_app.py — Main Python app (Tkinter UI) that connects to MySQL and runs CRUD and reporting queries.
  - Buttons for: Create Book / Publisher / Patron; Read Books / Publishers / Patrons; Update Book / Publisher / Patron; Delete Book / Publisher / Patron.
  - Extra queries: list books with authors, books by a specific publisher, count books by author, titles by a specific author.
- create_sql.md — CREATE DATABASE / CREATE TABLE statements for the schema (Books, Authors, BookAuthors, Publishers, BookPublishers, Patrons).
- insert_sql.md — INSERT statements with sample data.
- crud_sql.md — Example CRUD SQL statements used for demonstration.
- db_description.md — Human-readable description of tables, keys, FDs and normalization notes.
- README.md / readme.md — small notes.

Requirements
- Python 3.x
- mysql-connector-python (install with pip)
- MySQL server (or compatible) to host the lib_database_system database

Notes / usage
- The app uses mysql.connector to execute SQL directly; queries are predefined in the script and operate on fixed example IDs (e.g., BookID = 6 for create/update/delete demo entries).
- Output of queries is shown in the small Tkinter UI label and also printed to the console.
- The SQL files are provided so you can recreate the schema and sample data before running the Python app.
