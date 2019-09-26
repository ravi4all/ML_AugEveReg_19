import pymysql

# connect - will create the connection
# host = localhost => path of database, in this case our system is server, so localhost
# port - 3306 => default port of mysql, we change it from my.ini file
# user - root => user name for database is root
# database - music_player => name of our database
# autocommit - True => whenever we do any change in table, our database will auto commit the changes
connection = pymysql.connect(host="localhost",port=3306,user="root",database="music_player",
                             autocommit=True)

# connection.cursor - for every query there is a cursor object created for each connection
cursor = connection.cursor()

song = "Channa Mereya"
singer = "Arijit Singh"
movie = "ADHM"

query = "insert into playlist values (%s,%s,%s)"
cursor.execute(query, (song,singer,movie))
print("Data Inserted Successfully...")