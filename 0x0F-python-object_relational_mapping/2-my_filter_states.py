#!/usr/bin/python3

"""
This script takes an argument and displays all values in the states table of hbtn_0e_0_usa where the name matches the argument.
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
    
    # Execute a query to retrieve all rows from the 'states' table where the name matches the argument (case-sensitive) and order them by id
    db.execute("""SELECT * FROM states
    WHERE name LIKE BINARY '{}' ORDER BY id"""
               .format(state))
    
    # Fetch all results
    r = db.fetchall()
    
    # Iterate through the results and print them
    for i in r:
        print(i)

