from typing import Optional
from fastapi import FastAPI


import requests

from db import db
import env

app = FastAPI()
database= db()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data")
def read_root():
  # r = requests.get(env.DataAPI) 
  # data = r.json() 
  # return data
  db.insertmapCoordinate([1.1,2.1,3.1,4.1])

@app.get("/district")
def read_root():
  r = requests.get(env.DistrictList)
  data = r.json() 

  for index in data:
    districtid=index["id"]
    bbox=index["bbox"]
    name=index["title_en"]
    code =index["code"]
    centroid=index["centroid"]["coordinates"]
    province=index["province"]

    bboxkey= db.insertmapCoordinate(bbox)
    # print(bboxkey)
    centroidkey= db.insertCoordinate(centroid)
    # print(centroidkey)

    db.insertDistrict(districtid, name,"",code,province,centroidkey,bboxkey)
    # break

  return True
  # db.insertmapCoordinate([1.1,2.1,3.1,4.1])

  


  # for x in data:
    # print(x)
  # print(insertsql)
  
  # return x
  # mycursor.close()


  # sql="select *from mapCoordinate"
  # mycursor.execute(sql)

  # print( mycursor.fetchall())

@app.get("/municipality")
def read_root():
  r = requests.get(env.MunicipalityList)
  data = r.json() 

  for index in data:
    municipalityid=index["id"]
    bbox=index["bbox"]
    name=index["title_en"]
    code =index["code"]
    typ=index["type"]
    centroid=index["centroid"]["coordinates"]
    
    print(code)
    bboxkey= db.insertmapCoordinate(bbox)
    # print(bboxkey)
    centroidkey= db.insertCoordinate(centroid)
    # print(centroidkey)

    db.insertMunicipality(municipalityid,bboxkey,name,"",code,typ,centroidkey)
    # break

  return True

@app.get("/location")
def read_root():
  r = requests.get(env.MunicipalityList)
  data = r.json() 

  for index in data:
    municipalityid=index["id"]
    districtid=index["district"]
    db.insertLocation(municipalityid,districtid)
    # break

  return True


@app.get("/individual")
def read_root():
  r = requests.get(env.IndividualList)
  data = r.json() 

  for index in data:
    print (index)
    status=index["currentState"]
    isreinfected=True#index["isReinfected"]
    typ=index["type"]
    deadon= index["deathOn"]
    reportedon=index["reportedOn"]
    recoveredon=index["recoveredOn"]
    # print(status)
    # print(isreinfected)
    # print(typ)
    # print(deadon)
    # print(recoveredon)
    statusid= db.insertStatus(status,isreinfected,typ,deadon,reportedon,recoveredon)
    
    centroid=index["point"]["coordinates"]
    coordinateid= db.insertCoordinate(centroid)
    
    id2=index["id"]
    value=index["label"]
    gender=index["gender"]
    age=index["age"]
    occupation=index["occupation"]
    createdon=index["createdOn"]
    modifiedon=index["modifiedOn"]
    # statusid
    # centroidkey
    # print(index["municipality"])
    locationid=db.searchLocation(index["municipality"])
    
    print(id2)
    print(value)
    print(gender)
    print(age)
    print(occupation)
    print(createdon)
    print(modifiedon)
    print(locationid)

    db.insertIndividual(id2,value,gender,age,occupation,createdon,modifiedon,locationid,statusid,coordinateid)
    # break

  return True



@app.get("/individualcheck")
def read_root():
  r = requests.get(env.IndividualList)
  data = r.json() 

  datatemp= db.readIndividualid()
  dataDB=[]
  for datum in datatemp:
    if datum[0]!= None:
      dataDB.append(datum[0])
  print(dataDB)
  cnt=0

  for index in data:
    # print (index)
    id2=index["id"]
    status=index["currentState"]
    isreinfected=True#index["isReinfected"]
    typ=index["type"]
    deadon= index["deathOn"]
    reportedon=index["reportedOn"]
    recoveredon=index["recoveredOn"]

    if (id2 in dataDB):
      print(id2)
      print("pass")
      continue
    
    print(status)
    print(isreinfected)
    print(typ)
    print(deadon)
    print(recoveredon)
    statusid= db.insertStatus(status,isreinfected,typ,deadon,reportedon,recoveredon)
    
    centroid=index["point"]["coordinates"]
    coordinateid= db.insertCoordinate(centroid)
    
    
    value=index["label"]
    gender=index["gender"]
    age=index["age"]
    occupation=index["occupation"]
    createdon=index["createdOn"]
    modifiedon=index["modifiedOn"]
    # statusid
    # centroidkey
    # print(index["municipality"])
    locationid=db.searchLocation(index["municipality"])
    
    print(id2)
    print(value)
    print(gender)
    print(age)
    print(occupation)
    print(createdon)
    print(modifiedon)
    print(locationid)

    db.insertIndividual(id2,value,gender,age,occupation,createdon,modifiedon,locationid,statusid,coordinateid)
    # break

  return True


# @app.get("/individualupdate")
# def read_root():
#   r = requests.get(env.IndividualList)
#   data = r.json() 

#   datatemp= db.readIndividualid()
#   dataDB=[]
#   for datum in datatemp:
#     if datum[0]!= None:
#       dataDB.append(datum[0])
#   print(dataDB)
  
#   for index in data:
#     print (index)
#     id2=index["id"] 
#     status=index["currentState"]
#     isreinfected=True#index["isReinfected"]
#     typ=index["type"]
#     deadon= index["deathOn"]
#     reportedon=index["reportedOn"]
#     recoveredon=index["recoveredOn"]
#     if (id2 in dataDB):
#       pass
#     else:
#       break
#     statusid= db.insertStatus(status,isreinfected,typ,deadon,reportedon,recoveredon)
    
#     centroid=index["point"]["coordinates"]
#     coordinateid= db.insertCoordinate(centroid)
    
    
#     value=index["label"]
#     gender=index["gender"]
#     age=index["age"]
#     occupation=index["occupation"]
#     createdon=index["createdOn"]
#     modifiedon=index["modifiedOn"]
#     # statusid
#     # centroidkey
#     # print(index["municipality"])
#     locationid=db.searchLocation(index["municipality"])
    
#     print(id2)
#     print(value)
#     print(gender)
#     print(age)
#     print(occupation)
#     print(createdon)
#     print(modifiedon)
#     print(locationid)

#     db.insertIndividual(id2,value,gender,age,occupation,createdon,modifiedon,locationid,statusid,coordinateid)
#     # break

#   return True