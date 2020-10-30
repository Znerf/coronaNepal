
import mysql.connector

mydb = mysql.connector.connect(
            host=,
            user=,
            password=,
            database=
        )
mycursor = mydb.cursor()




class db:
    def __init__(self):
        pass

    def insertmapCoordinate(b):
        sql = ("""INSERT INTO mapCoordinate (bbox1, bbox2, bbox3, bbox4) VALUES (%s,%s,%s,%s) """)
       
        val=(b[0],b[1],b[2],b[3])
        mycursor.execute(sql, val)
        mydb.commit()

