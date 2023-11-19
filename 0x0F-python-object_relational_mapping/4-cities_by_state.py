#!/usr/bin/python3
"""Script that lists all states from a database."""


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

    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
        cities INNER JOIN states ON states.id = cities.state_id
        ORDER BY cities.id ASC;""")

    m = cursor.fetchall()
    for i in m:
        print(i)

    cursor.close()
    db_connection.close()
