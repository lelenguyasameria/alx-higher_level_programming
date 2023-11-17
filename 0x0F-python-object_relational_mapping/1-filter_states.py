#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

    Usage:
        ./script.py <username> <password> <db_name>

    Args:
        <username>: MySQL username.
        <password>: MySQL password.
        <db_name>: Database name.

    Output:
        Prints the list of states with names starting with N in the format (id, 'state_name').
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()

        # Execute the SQL query to fetch states with names starting with N
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
        cur.execute(query)

        # Fetch all the rows and display the results
        rows = cur.fetchall()
        for row in rows:
            print("({}, '{}')".format(row[0], row[1]))

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the cursor and connection
        if cur:
            cur.close()
        if db:
            db.close()

