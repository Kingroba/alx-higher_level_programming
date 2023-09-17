#!/usr/bin/python3

"""
This script takes the name of a state as an argument and lists all cities of that state using the database hbtn_0e_4_usa.
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
    
    # Execute a query to retrieve the names of cities from the 'cities' table where the associated state matches the argument, and order them by cities.id
    db.execute("""
    SELECT cities.name
    FROM cities
    JOIN states
    ON state_id=states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id
    """, (state,))
    
    # Fetch all results
    r = db.fetchall()
    
    # Print the names of the cities, joined by commas
    print(", ".join([row[0] for row in r]))

