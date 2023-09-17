#!/usr/bin/python3

"""
This script performs a SQL query to retrieve all rows from the 'states' table in hbtn_0e_0_usa where the name matches the argument, using parameterized queries to prevent SQL injection.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    user, password, database, state = argv[1], argv[2], argv[3], argv[4]
    
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=password, db=database)
    
    # Create a cursor object to execute queries
    db = db.cursor()
    
    # Execute a parameterized query to retrieve all rows from the 'states' table where the name matches the argument and order them by id
    db.execute("""SELECT * FROM states WHERE name=%s ORDER BY id""", (state,))
    
    # Fetch all results
    r = db.fetchall()
    
    # Iterate through the results and print them
    for i in r:
        print(i)

