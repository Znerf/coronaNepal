from typing import Optional
from fastapi import FastAPI

import requests

from db import db




app = FastAPI()
database= db()



api="https://data.nepalcorona.info/api/v1/covid"

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data")
def read_root():
  # r = requests.get(api) 
  # data = r.json() 

  db.insertmapCoordinate([1.1,2.1,3.1,4.1])

  


  # for x in data:
    # print(x)
  # print(insertsql)
  
  # return x
  # mycursor.close()


  # sql="select *from mapCoordinate"
  # mycursor.execute(sql)

  # print( mycursor.fetchall())
