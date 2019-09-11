dbconfig = {
    'user' : 'smartplantCMP',
    'password' : 'planten',
    'host' : 'localhost',
    'raise_on_warnings' : True,
}

try:
    mariadb_connection = mariadb.connect(**dbconfig)
    if verbose:
        print("Database connected")
except mariadb.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Error: {}".format(err))
    sys.exit(2)
# create the database cursor for executing SQL queries
cursor = mariadb_connection.cursor()
# turn on autocommit
#cursor.autocommit = True

id = cursor.execute("SELECT id FROM meting")
name = cursor.execute("SELECT naam FROM meting ")
temp = cursor.execute("SELECT temp FROM meting")
vocht = cursor.execute("SELECT vocht FROM meting")
licht = cursor.execute("SELECT licht FROM meting")

namePlant = cursor.execute("SELECT naam FROM meting ")
tempPlant = cursor.execute("SELECT temp FROM meting")
vochtPlant = cursor.execute("SELECT vocht FROM meting")
lichtPlant = cursor.execute("SELECT licht FROM meting")

tempResult
vochtResult
lichtResult

if name==namePlant :
    if temp > tempPlant :
        tempResult = True
    else :
        tempResult = False
    if vocht> vochtPlant:
        tempResult