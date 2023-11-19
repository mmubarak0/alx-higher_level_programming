#!/usr/bin/python3
"""Script that lists all states with a name starting with N."""


if __name__ == '__main__':
    import sys
    import MySQLdb

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host_name = "localhost"
    port = 3306

    try:
        db_connection = MySQLdb.connect(
            host_name, user, password, db_name, port=port
        )
    except Exception as e:
        print(e)
        exit(0)

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    m = cursor.fetchall()
    for i in m:
        if (i[1][0] == "N"):
            print(i)

    cursor.close()
    db_connection.close()
