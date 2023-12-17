#!/usr/bin/python3
"""Lists all cities by state passed by user"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("""
           SELECT cities.id, cities.name, states.name FROM cities
           LEFT JOIN states ON cities.state_id = states.id
           WHERE states.name = %s
           ORDER BY cities.id ASC;
           """, (argv[4],))
    query_rows = cursor.fetchall()
    print(", ".join([row[1] for row in query_rows]))
    cursor.close()
    connection.close()
