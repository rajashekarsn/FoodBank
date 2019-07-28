import sqlite3

conn = sqlite3.connect('testsqllite3.db')

print   ("Created database successfully")


c = conn.cursor()

# #create a table
# c.execute("""CREATE TABLE books
#            (title text, author text)""")

# # alter a table, add new column
# c.execute("""ALTER TABLE books
#             ADD publisher text""")

# # insert some data
# c.execute("INSERT INTO books VALUES ('Pride and Prejudice', 'Jane Austen','abc pub')")

# save data to database
# conn.commit()

# insert multiple records using the more secure "?" method
books = [('Harry Potter', 'J.K Rowling','pub1'),
          ('The Lord of the Rings', 'J. R. R. Tolkien','pub2'),
          ('The Hobbit','J. R. R. Tolkien','null')]
c.executemany("INSERT INTO books VALUES (?,?,?)", books)
conn.commit()