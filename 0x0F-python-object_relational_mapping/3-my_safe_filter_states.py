#!/usr/bin/python3
"""Lists all states starting with passed arg, prevents injection"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY\
                    states.id ASC", (argv[4], ))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
