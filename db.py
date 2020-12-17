
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
        # OUTPUT Inserted.mapid
        val=(b[0],b[1],b[2],b[3])
        mycursor.execute(sql, val)
        mydb.commit()
        
        return mycursor.lastrowid

    def insertCoordinate(b):
        sql = ("""INSERT INTO coordinate (x, y) VALUES (%s,%s) """)

        val=(b[0],b[1])
        mycursor.execute(sql, val)
        mydb.commit()
        
        return mycursor.lastrowid

    def insertDistrict(districtid,name,nepaliname,code,province,centroidcoordinate,bbox):
        sql = ("""INSERT INTO district (`districtid`,`name`,`nepali-name`,`code`,`province`,`centroid-coordinate`,`bbox`) VALUES (%s,%s,%s,%s,%s,%s,%s) """)

        val=(districtid, name,nepaliname,code,province,centroidcoordinate,bbox)
        mycursor.execute(sql, val)
        mydb.commit()
        
        return mycursor.lastrowid

    def insertMunicipality(municipalityid,bboxkey,name,nepaliname,code,typ,centroidkey):
        sql = ("""INSERT INTO municipality (`municipalityid`,`bbox`,`name`,`nepali-name`,`code`,`type`,`centroid-coordinate`) VALUES (%s,%s,%s,%s,%s,%s,%s) """)

        val=(municipalityid,bboxkey,name,nepaliname,code,typ,centroidkey)
        mycursor.execute(sql, val)
        mydb.commit()
        
        return mycursor.lastrowid
    
    def insertLocation(municipalityid,districtid):
        sql = ("""INSERT INTO location (`municipality-id`,`district-id`) VALUES (%s,%s) """)

        val=(municipalityid,districtid)
        mycursor.execute(sql, val)
        mydb.commit()
        
        return True
    
    def insertStatus(status,isreinfected,typ,deadon,reportedon,recoveredon):
        sql = ("""INSERT INTO status (`status`,`is-reinfected`,`type`,`deadon`,`reportedon`,`recoveredon`) VALUES (%s,%s,%s,%s,%s,%s) """)

        val=(status,isreinfected,typ,deadon,reportedon,recoveredon)
        mycursor.execute(sql, val)
        mydb.commit()
        
        return mycursor.lastrowid
    
    def searchLocation(municipality):
        sql = ("SELECT locationid FROM location WHERE `municipality-id` = %s")

        val=(municipality,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()

        mydb.commit()
        
        return myresult[0][0]
    
    def insertIndividual(id2,value,gender,age,occupation,createddate,modifieddate,locationid,statusid,coordinateid):

        sql = ("""INSERT INTO individual (`id2`,`value`,`gender`,`age`,`occupation`,`created-date`,`modified-date`,`location-id`,`status-id`,`coordinate-id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """)

        val=(id2,value,gender,age,occupation,createddate,modifieddate,locationid,statusid,coordinateid)
        mycursor.execute(sql, val)
        mydb.commit()
        
        return True

    def readIndividualid():
        sql = ("SELECT id2 FROM individual")

        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        mydb.commit()
        
        return myresult
