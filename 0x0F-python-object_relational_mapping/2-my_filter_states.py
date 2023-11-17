#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches the provided argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Script that displays all values in the states table of hbtn_0e_0_usa where name matches the provided argument.

    Usage:
        ./script.py <username> <password> <db_name> <state_name>

    Args:
        <username>: MySQL username.
        <password>: MySQL password.
        <db_name>: Database name.
        <state_name>: State name to be searched.

    Output:
        Prints the list of values where the name matches the provided argument.
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()

        # Prepare the SQL query using user input
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
        # Fetch all the rows and display the results
        rows = cur.fetchall()
        for row in rows:
            print(row)


    finally:
        # Close the cursor and connection
        cur:
            cur.close()
        db:
            db.close()

