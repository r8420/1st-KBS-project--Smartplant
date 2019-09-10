#!/usr/bin/python3

# import connection module; name it mariadb
import mysql.connector as mariadb
import json;

# initialize
data = []

# connect to the database
mariadb_connection = mariadb.connect(
    user='smartplant',
    password='planten',
    database='smartplant')

# create a cursor object for executing queries
cursor = mariadb_connection.cursor()

# prepare a select query (only the 100 last items)
stmt = "SELECT UNIX_TIMESTAMP(tijd) as unixtime, waarde FROM meting ORDER BY id ASC"

# execute the query (parameter must be a tuple)
cursor.execute(stmt)

num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description] 

# returned rows (tuples)
rows = cursor.fetchall()

# close cursor and database
cursor.close()
mariadb_connection.close()

output_json = []
for row in rows:
    output_json.append(dict(zip(field_names,row)))

print("Content-type: application/json\n")
print(json.dumps(output_json))
# done
