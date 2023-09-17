#!/usr/bin/python3

"""
This script lists all cities from the database hbtn_0e_4_usa.
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
    
    # Execute a query to retrieve specific columns from the 'cities' and 'states' tables, joining them based on the state_id and ordering by cities.id
    db.execute("""SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON state_id=states.id ORDER BY cities.id""")
    
    # Fetch all results
    r = db.fetchall()
    
    # Iterate through the results and print them
    for i in r:
        print(i)

