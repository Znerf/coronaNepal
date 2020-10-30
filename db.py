
import mysql.connector
import env

mydb = mysql.connector.connect(
            host=env.HOST,
            user=env.USER,
            password=env.PASSWORD,
            database=env.DATABASE
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

