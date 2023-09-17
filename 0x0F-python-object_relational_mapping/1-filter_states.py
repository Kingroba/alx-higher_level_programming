#!/usr/bin/python3

"""
This script lists all states with a name starting with 'N'
(uppercase 'N') from the database hbtn_0e_0_usa.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database)
    
    # Create a cursor object to execute queries
    db = db.cursor()
    
    # Execute a query to retrieve all rows from the 'states' table where the name starts with 'N' (case-insensitive) and order them by id
    db.execute("""SELECT * FROM states
    WHERE REGEXP_LIKE(name, '^N', 'c') ORDER BY id""")
    
    # Fetch all results
    r = db.fetchall()
    
    # Iterate through the results and print them
    for i in r:
        print(i)

