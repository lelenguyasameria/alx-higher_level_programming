#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def list_states(username, password, db_name):
    """
    List all states from the database hbtn_0e_0_usa.
    """
    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv,
            passwd=sys.argv,
            db=sys.argv
        )

        cursor = connection.cursor()

        query = "SELECT * FROM states ORDER BY states.id"
        cursor.execute(query)

        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:]

    list_states(username, password, db_name)

