#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database)
    
    # Execute a query to retrieve all rows from the 'states' table and order them by id
    db.query("SELECT * FROM states ORDER BY id")
    
    # Store the result of the query
    r = db.store_result()
    
    # Fetch all rows from the result
    t = r.fetch_row(maxrows=0)
    
    # Iterate through the rows and print them
    for i in t:
        print(i)
